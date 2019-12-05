from eventsourcing.exceptions import EntityIsDiscarded
from eventsourcing.domain.model.events import DomainEvent
from eventsourcing.domain.model.events import publish
from eventsourcing.domain.model.events import subscribe, unsubscribe
from eventsourcing.utils.topic import get_topic
from eventsourcing.domain.model.entity import VersionedEntity
from eventsourcing.domain.model.entity import DomainEntity
from eventsourcing.domain.model.entity import TimestampedVersionedEntity
from eventsourcing.domain.model.entity import TimestampedEntity
from uuid import uuid4
from uuid import UUID

entity_id = uuid4()

entity1 = DomainEntity(id=entity_id)
entity2 = VersionedEntity(id=entity_id, __version__=1)
entity3 = TimestampedEntity(id=entity_id, __created_on__=123)
entity4 = TimestampedVersionedEntity(
    id=entity_id, __version__=1, __created_on__=123)


entity_id = UUID('b81d160d-d7ef-45ab-a629-c7278082a845')

created = VersionedEntity.Created(
    originator_version=0,
    originator_id=entity_id,
    originator_topic=get_topic(VersionedEntity)
)

attribute_a_changed = VersionedEntity.AttributeChanged(
    name='a',
    value=1,
    originator_version=1,
    originator_id=entity_id,
)

attribute_b_changed = VersionedEntity.AttributeChanged(
    name='b',
    value=2,
    originator_version=2,
    originator_id=entity_id,
)

entity_discarded = VersionedEntity.Discarded(
    originator_version=3,
    originator_id=entity_id,
)

'''
__mutate__()
does the projection of the events into the entity itself
if its none it projects entity object itself(self)

The class that is instantiated is determined by the event’s originator_topic

'''

entity = created.__mutate__()

assert entity.__version__ == 0


entity = attribute_a_changed.__mutate__(entity)
assert entity.__version__ == 1
assert entity.a == 1

entity = attribute_b_changed.__mutate__(entity)
assert entity.__version__ == 2
assert entity.b == 2


# Factory methods

entity = DomainEntity.__create__()
assert entity.id
assert entity.__class__ is DomainEntity


entity = VersionedEntity.__create__()
assert entity.id
assert entity.__version__ == 0
assert entity.__class__ is VersionedEntity


entity = TimestampedEntity.__create__()
assert entity.id
assert entity.__created_on__
assert entity.__last_modified__
assert entity.__class__ is TimestampedEntity


entity = TimestampedVersionedEntity.__create__()
assert entity.id
assert entity.__created_on__
assert entity.__last_modified__
assert entity.__version__ == 0
assert entity.__class__ is TimestampedVersionedEntity


entity.__trigger_event__(entity.AttributeChanged, name='c', value=3)
entity.c


received_events = []


def receive_event(event):
    received_events.append(event)


def is_domain_event(event):
    return isinstance(event, DomainEvent)


subscribe(handler=receive_event, predicate=is_domain_event)
entity = VersionedEntity.__create__(entity_id)
entity.__change_attribute__(name='full_name', value='Mr Boots')
# events logged at received_events

received_events[0]
received_events[2]

# Clean up.
unsubscribe(handler=receive_event, predicate=is_domain_event)
del received_events[:]  # received_events.clear()


# __discard__() triggers a Discarded event, after which the entity is unavailable for further changes.


entity.__discard__()

# Fail to change an attribute after entity was discarded.
try:
    entity.__change_attribute__('full_name', 'Mr Boots')
except EntityIsDiscarded:
    pass
else:
    raise Exception("Shouldn't get here")


# Custom Entity

class User(VersionedEntity):
    def __init__(self, full_name, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.full_name = full_name