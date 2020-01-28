# pip3 install --upgrade eventsourcing==8.0.0

from uuid import uuid4

from eventsourcing.application.policies import PersistencePolicy
from eventsourcing.domain.model.entity import DomainEntity
from eventsourcing.infrastructure.eventstore import EventStore
from eventsourcing.infrastructure.repositories.array import BigArrayRepository
from eventsourcing.infrastructure.sequenceditem import StoredEvent
from eventsourcing.infrastructure.sequenceditemmapper import SequencedItemMapper
from eventsourcing.infrastructure.sqlalchemy.datastore import SQLAlchemyDatastore, SQLAlchemySettings
from eventsourcing.infrastructure.sqlalchemy.manager import SQLAlchemyRecordManager
from eventsourcing.infrastructure.sqlalchemy.records import StoredEventRecord

# Setup the database.
datastore = SQLAlchemyDatastore(
    settings=SQLAlchemySettings(),
    tables=[StoredEventRecord],
)
datastore.setup_connection()
datastore.setup_tables()

# Setup the record manager.
record_manager = SQLAlchemyRecordManager(
    session=datastore.session,
    record_class=StoredEventRecord,
    sequenced_item_class=StoredEvent,
    contiguous_record_ids=True,
    application_name=uuid4().hex,
)

# Setup a sequenced item mapper.
sequenced_item_mapper = SequencedItemMapper(
    sequenced_item_class=StoredEvent,
)

# Setup the event store.
event_store = EventStore(
    record_manager=record_manager,
    event_mapper=sequenced_item_mapper
)

# Set up a persistence policy.
persistence_policy = PersistencePolicy(
    event_store=event_store,
    persist_event_type=DomainEntity.Event
)

from eventsourcing.domain.model.entity import VersionedEntity

notifications = record_manager.get_notifications()

first_entity = VersionedEntity.__create__()

notifications = record_manager.get_notifications(start=0, stop=5)

from eventsourcing.application.notificationlog import RecordManagerNotificationLog

# Construct notification log(it updates dynamically while notifications above updated by each explicit implementations ).
notification_log = RecordManagerNotificationLog(record_manager, section_size=10)
section = notification_log['current']
print(section.section_id )
print(len(notification_log.get_items(start=0,stop=1000)))

second_entity = VersionedEntity.__create__()
section = notification_log['current']
print(section.section_id )
print(len(notification_log.get_items(start=0,stop=1000)))

third_entity = VersionedEntity.__create__()
section = notification_log['current']
print(section.section_id )
print(len(notification_log.get_items(start=0,stop=1000)))

#each section has its own items (section as linked list of objects)
print([n['originator_id'] for n in section.items])


def resolve_notifications(notifications):
    return [
        sequenced_item_mapper.event_from_topic_and_state(
            topic=notification['topic'],
            state=notification['state']
        ) for notification in notifications
    ]

domain_events = resolve_notifications(section.items)


# Additional big array
from uuid import uuid4
from eventsourcing.domain.model.array import BigArray
from eventsourcing.infrastructure.repositories.array import BigArrayRepository


repo = BigArrayRepository(
    event_store=event_store,
    array_size=10000
)

big_array = repo[uuid4()]
big_array.append('item0')
big_array.append('item1')
big_array.append('item2')
big_array.append('item3')

notification_log.get_items(start=0,stop=1000)[3]['state']
domain_events = resolve_notifications(notification_log['current'].items)
print(domain_events[3].item)
# In this event [4] Item append done to big array entity
print(domain_events[4].item)


from eventsourcing.application.notificationlog import BigArrayNotificationLog

# Construct notification log.
big_array_notification_log = BigArrayNotificationLog(big_array, section_size=5)

# Get the "current "section from the big array notification log.
section = big_array_notification_log['current']
section.items

# Remote notification logs
# check class RemoteNotificationLog


import json

from eventsourcing.interface.notificationlog import NotificationLogView
from eventsourcing.utils.transcoding import ObjectJSONEncoder, ObjectJSONDecoder

view = NotificationLogView(
    notification_log=notification_log,
    json_encoder=ObjectJSONEncoder()
)
# Serizlized section as bellow
view.present_resource('section_size')
view.present_resource('current')
view.present_resource('1,5')


section_json = view.present_resource('1,5')

# Can be dict.
section_dict = ObjectJSONDecoder().decode(section_json.decode('utf-8'))
len(section_dict['items'])
print(section_dict['items'][1]['topic'])

# Also resolves dict2event
domain_events = resolve_notifications(section_dict['items'])

# NotificationLogReader effectively functions as an iterator, yielding 
# a continuous sequence of notifications that it discovers from the 
# sections of a notification log, local or remote.

from eventsourcing.application.notificationlog import NotificationLogReader

# Construct log reader.
reader = NotificationLogReader(notification_log)
reader.seek(0)
all_notifications = reader.read_list()
domain_events = resolve_notifications(all_notifications)

# events of an application can be followed
reader.seek(0)
few_notifications=reader.read_list(2)
few_more_notifications=reader.read_list(2)

# Clean up.
persistence_policy.close()