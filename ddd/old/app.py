# eventsourcing==7.2.4

from eventsourcing.utils.random import encoded_random_bytes

# Keep this safe (random bytes encoded with Base64).
cipher_key = encoded_random_bytes(num_bytes=32)

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