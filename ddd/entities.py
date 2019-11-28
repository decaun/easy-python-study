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
entity4 = TimestampedVersionedEntity(id=entity_id, __version__=1, __created_on__=123)

from eventsourcing.utils.topic import get_topic

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

