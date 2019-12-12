from eventsourcing.application.notificationlog import RecordManagerNotificationLog
from eventsourcing.infrastructure.integersequencegenerators.base import SimpleIntegerSequenceGenerator
from eventsourcing.domain.model.array import BigArray
from eventsourcing.domain.model.entity import VersionedEntity
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
    sequenced_item_mapper=sequenced_item_mapper
)

# Set up a persistence policy.
persistence_policy = PersistencePolicy(
    event_store=event_store,
    persist_event_type=DomainEntity.Event
)


notifications = record_manager.get_notifications()

assert len(notifications) == 0, notifications

first_entity = VersionedEntity.__create__()

notifications = record_manager.get_notifications(start=0, stop=5)

assert len(notifications) == 1, notifications


repo = BigArrayRepository(
    event_store=event_store,
    array_size=10000
)

big_array = repo[uuid4()]
big_array.append('item0')
big_array.append('item1')
big_array.append('item2')
big_array.append('item3')


# generates a contiguous sequence of integers that
# can be shared across multiple threads in the same process


integers = SimpleIntegerSequenceGenerator()
generated = []
for i in integers:
    if i >= 5:
        break
    generated.append(i)

expected = list(range(5))


# Construct notification log.
notification_log = RecordManagerNotificationLog(record_manager, section_size=5)


# Get the "current" section from the record notification log.
section = notification_log['current']
assert section.section_id == '6,10', section.section_id
assert section.previous_id == '1,5', section.previous_id
assert section.next_id == None
print('{}'.format(section.items))
# Recover events from notification_log


def resolve_notifications(notifications):
    return [
        sequenced_item_mapper.event_from_topic_and_state(
            topic=notification['topic'],
            state=notification['state']
        ) for notification in notifications
    ]


# Resolve a section of notifications into domain events.
domain_events = resolve_notifications(section.items)

print('{}'.format(domain_events))
