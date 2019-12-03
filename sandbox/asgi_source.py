from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import EmailStr
from eventsourcing.domain.model.events import subscribe
from eventsourcing.domain.model.events import publish
from eventsourcing.domain.model.events import EventWithOriginatorID
from eventsourcing.domain.model.events import unsubscribe
from uuid import uuid4

app = FastAPI()
received_events = []


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print('Size of log: {}'.format(len(received_events)))
    return user_in_db

class CustomEvent(EventWithOriginatorID):
    def __init__(self,originator_id):
        super().__init__(originator_id)
        print('Custom event happened! ID: {}'.format(self.originator_id))


def receive_event(event):
    received_events.append(event)

def is_domain_event(event):
    return isinstance(event, CustomEvent)

subscribe(handler=receive_event, predicate=is_domain_event)

@app.post("/user/", response_model=UserOut)
async def create_user(*, user_in: UserIn):
    user_saved = fake_save_user(user_in)
    publish(event=CustomEvent(originator_id=uuid4()))
    return user_saved


