from eventsourcing.domain.model.events import subscribe
from eventsourcing.domain.model.events import publish
from eventsourcing.domain.model.events import EventWithOriginatorID
from eventsourcing.domain.model.events import unsubscribe
from uuid import uuid4

class CustomEvent(EventWithOriginatorID):
    def __init__(self,originator_id):
        super().__init__(originator_id)
        print('Custom event happened! ID: {}'.format(self.originator_id))

received_events = []

def receive_event(event):
    received_events.append(event)

def is_domain_event(event):
    return isinstance(event, CustomEvent)

print("subscribed")
subscribe(handler=receive_event, predicate=is_domain_event)


publish(event=CustomEvent(originator_id=uuid4()))
print('Size of log: {}'.format(len(received_events)))

publish(event=CustomEvent(originator_id=uuid4()))
print('Size of log: {}'.format(len(received_events)))

print("unsubscribed")
unsubscribe(handler=receive_event, predicate=is_domain_event)

publish(event=CustomEvent(originator_id=uuid4()))
print('Size of log: {}'.format(len(received_events)))


