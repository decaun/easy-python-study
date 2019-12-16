# eventsourcing==7.2.4


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
received_events[1]

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

from eventsourcing.domain.model.decorators import attribute


class User(VersionedEntity):

    def __init__(self, full_name, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._full_name = full_name

    @attribute
    def full_name(self):
        '''
        The full name of the user (an event-sourced attribute).
        '''


subscribe(handler=receive_event, predicate=is_domain_event)

# Publish a Created event.
user = User.__create__(full_name='Mrs Boots')

# Publish an AttributeChanged event.
user.full_name = 'Mr Boots'

assert len(received_events) == 2
assert received_events[0].__class__ == VersionedEntity.Created
assert received_events[0].full_name == 'Mrs Boots'
assert received_events[0].originator_version == 0
assert received_events[0].originator_id == user.id

assert received_events[1].__class__ == VersionedEntity.AttributeChanged
assert received_events[1].value == 'Mr Boots'
assert received_events[1].name == '_full_name'
assert received_events[1].originator_version == 1
assert received_events[1].originator_id == user.id

# Clean up.
unsubscribe(handler=receive_event, predicate=is_domain_event)
del received_events[:]  # received_events.clear()


# Custom Command

class User(VersionedEntity):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._password = None

    def set_password(self, raw_password):
        # Do some work using the arguments of a command.
        password = self._encode_password(raw_password)

        # Change private _password attribute.
        self.__change_attribute__('_password', password)

    def check_password(self, raw_password):
        password = self._encode_password(raw_password)
        return self._password == password

    def _encode_password(self, password):
        return ''.join(reversed(password))


user = User(id='1', __version__=0)

user.set_password('password')
assert user.check_password('password')

# Custom Event

class World(VersionedEntity):

    def __init__(self, *args, **kwargs):
        super(World, self).__init__(*args, **kwargs)
        self.history = []

    def make_it_so(self, something):
        # Do some work using the arguments of a command.
        what_happened = something

        # Trigger event with the results of the work.
        self.__trigger_event__(World.SomethingHappened, what=what_happened)

    class SomethingHappened(VersionedEntity.Event):
        """Triggered when something happens in the world."""
        def mutate(self, obj):
            obj.history.append(self.what)


# Base aggregate
# the method __save__(), which publishes all pending 
# events to the publish-subscribe mechanism as a single list

from eventsourcing.domain.model.aggregate import BaseAggregateRoot


class World(BaseAggregateRoot):
    """
    Example domain entity, with mutator function on domain event.
    """
    def __init__(self, *args, **kwargs):
        super(World, self).__init__(*args, **kwargs)
        self.history = []

    def make_things_so(self, *somethings):
        for something in somethings:
            self.__trigger_event__(World.SomethingHappened, what=something)

    class SomethingHappened(BaseAggregateRoot.Event):
        def mutate(self, obj):
            obj.history.append(self.what)

subscribe(handler=receive_event)

world = World.__create__()
world.make_things_so('dinosaurs', 'trucks', 'internet')
len(received_events)
len(world.__pending_events__)
world.__save__()

len(received_events)
len(world.__pending_events__)
