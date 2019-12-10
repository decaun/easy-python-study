from collections import namedtuple

SequencedItem = namedtuple('SequencedItem', ['sequence_id', 'position', 'topic', 'data'])

from eventsourcing.infrastructure.sequenceditem import SequencedItem

from uuid import uuid4

sequence1 = uuid4()

state = (
    '{"foo":"bar","position":0,"sequence_id":{"UUID":"%s"}}' % sequence1.hex
).encode('utf8')

sequenced_item1 = SequencedItem(
    sequence_id=sequence1,
    position=0,
    topic='eventsourcing.domain.model.events#DomainEvent',
    state=state,
)

from eventsourcing.infrastructure.sequenceditem import StoredEvent

aggregate1 = uuid4()

state = (
    '{"foo":"bar","originator_version":0,"originator_id":{"UUID":"%s"}}' % aggregate1.hex
).encode('utf8')

stored_event1 = StoredEvent(
    originator_id=aggregate1,
    originator_version=0,
    topic='eventsourcing.domain.model.events#DomainEvent',
    state=state,
)

from eventsourcing.infrastructure.sequenceditemmapper import SequencedItemMapper

sequenced_item_mapper = SequencedItemMapper()
domain_event = sequenced_item_mapper.event_from_item(sequenced_item1)
print(domain_event.foo)
recovered_state = sequenced_item_mapper.item_from_event(domain_event).state

from eventsourcing.domain.model.events import DomainEvent

domain_event1 = DomainEvent(
    originator_id=aggregate1,
    originator_version=1,
    foo='baz',
)

sequenced_item_mapper = SequencedItemMapper(
    sequence_id_attr_name='originator_id',
    position_attr_name='originator_version'
)

sequenced_item_mapper = SequencedItemMapper(
    sequenced_item_class=StoredEvent
)

print(domain_event1.foo)
domain_event1 = sequenced_item_mapper.event_from_item(stored_event1)

from eventsourcing.domain.model.events import Created
from eventsourcing.utils.topic import get_topic, resolve_topic

topic = get_topic(Created)

from eventsourcing.utils.topic import substitutions


substitutions['old_topic'] = 'new_topic'


from eventsourcing.utils.transcoding import ObjectJSONEncoder, ObjectJSONDecoder


class CustomObjectJSONEncoder(ObjectJSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return {'__set__': list(obj)}
        else:
            return super(CustomObjectJSONEncoder, self).default(obj)


class CustomObjectJSONDecoder(ObjectJSONDecoder):
    @classmethod
    def from_jsonable(cls, d):
        if '__set__' in d:
            return cls._decode_set(d)
        else:
            return ObjectJSONDecoder.from_jsonable(d)

    @staticmethod
    def _decode_set(d):
        return set(d['__set__'])


customized_sequenced_item_mapper = SequencedItemMapper(
    json_encoder_class=CustomObjectJSONEncoder,
    json_decoder_class=CustomObjectJSONDecoder,
    sequenced_item_class=StoredEvent,
)
state = (
    '{"foo":{"__set__":["bar","baz"]},"originator_version":0,"originator_id":{"UUID":"%s"}}' % sequence1.hex
).encode('utf8')
domain_event = customized_sequenced_item_mapper.event_from_item(
    StoredEvent(
        originator_id=sequence1,
        originator_version=0,
        topic='eventsourcing.domain.model.events#DomainEvent',
        state=state,
    )
)

print(domain_event.foo)
sequenced_item = customized_sequenced_item_mapper.item_from_event(domain_event)
print(sequenced_item.state)

from eventsourcing.utils.cipher.aes import AESCipher
from eventsourcing.utils.random import encode_random_bytes, decode_bytes

# Unicode string representing 256 random bits encoded with Base64.
cipher_key = encode_random_bytes(num_bytes=32)

# Construct AES-256 cipher.
cipher = AESCipher(cipher_key=decode_bytes(cipher_key))

# Encrypt some plaintext (using nonce arguments).
ciphertext = cipher.encrypt('plaintext')

# Decrypt some ciphertext.
plaintext = cipher.decrypt(ciphertext)

