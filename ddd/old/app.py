<<<<<<< HEAD:ddd/old/app.py
# eventsourcing==7.2.4

from eventsourcing.utils.random import encoded_random_bytes
=======
from eventsourcing.utils.random import encode_random_bytes
>>>>>>> f76fa2610ffb1b561774a926e5de2273a3102445:ddd/app.py

# Keep this safe (random bytes encoded with Base64).
cipher_key = encode_random_bytes(num_bytes=32)

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication
from eventsourcing.domain.model.aggregate import AggregateRoot

application = SQLAlchemyApplication(
    uri='sqlite:///:memory:',
    cipher_key=cipher_key,
    persist_event_type=AggregateRoot.Event,
)

from eventsourcing.infrastructure.eventstore import EventStore

assert isinstance(application.event_store, EventStore)

from eventsourcing.application.policies import PersistencePolicy

assert isinstance(application.persistence_policy, PersistencePolicy)

from eventsourcing.infrastructure.eventsourcedrepository import EventSourcedRepository

assert isinstance(application.repository, EventSourcedRepository)

obj = AggregateRoot.__create__()
obj.__change_attribute__(name='a', value=1)
assert obj.a == 1
obj.__save__()

# Check the repository has the latest values.
copy = application.repository[obj.id]
assert copy.a == 1

# Check the aggregate can be discarded.
copy.__discard__()
copy.__save__()
assert copy.id not in application.repository

# Check optimistic concurrency control is working ok.
from eventsourcing.exceptions import ConcurrencyError
try:
    obj.__change_attribute__(name='a', value=2)
    obj.__save__()
except ConcurrencyError:
    pass
else:
    raise Exception("Shouldn't get here")



# Follow application event notifications.
from eventsourcing.application.notificationlog import NotificationLogReader
reader = NotificationLogReader(application.notification_log)
notification_ids = [n['id'] for n in reader.read()]
assert notification_ids == [1, 2, 3], notification_ids

# - create two more aggregates
obj = AggregateRoot.__create__()
obj.__save__()

obj = AggregateRoot.__create__()
obj.__save__()

# - get the new event notifications from the reader
notification_ids = [n['id'] for n in reader.read()]
assert notification_ids == [4, 5], notification_ids


# Custom APP

from eventsourcing.domain.model.decorators import attribute

class CustomAggregate(AggregateRoot):
    def __init__(self, a, **kwargs):
        super(CustomAggregate, self).__init__(**kwargs)
        self._a = a

    @attribute
    def a(self):
        """Mutable attribute a."""


from eventsourcing.application.sqlalchemy import SQLAlchemyApplication


class MyApplication(SQLAlchemyApplication):
    persist_event_type = AggregateRoot.Event

    def create_aggregate(self, a):
        return CustomAggregate.__create__(a=1)

# Construct application object.
application = MyApplication(uri='sqlite:///:memory:')
# Create aggregate using application service, and save it.
aggregate = application.create_aggregate(a=1)
aggregate.__save__()
aggregate = application.repository[aggregate.id]

# Change attribute value.
aggregate.a = 2
aggregate.a = 3

# Don't forget to save!
aggregate.__save__()

# Retrieve again from repository.
aggregate = application.repository[aggregate.id]

# Discard the aggregate
# After being saved, a discarded aggregate will no longer be available in the repository.
'''
aggregate.__discard__()
aggregate.__save__()
'''

events = application.event_store.get_domain_events(originator_id=aggregate.id)
items = application.event_store.record_manager.list_items(aggregate.id)
event_records = application.event_store.record_manager.orm_query().all()

application.close()

