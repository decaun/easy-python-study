import asyncio
import faust
import random


class Add(faust.Record):
    a: int
    b: int


rpc_app = faust.App('RPCClientApp', reply_create_topic=True,
                    stream_buffer_maxsize=64, broker_commit_interval=0.001,
                    broker_commit_every=0.001)
topic = rpc_app.topic('adding', value_type=Add)


@rpc_app.agent(topic)
async def adding(stream):
    async for value in stream:
        # here we receive Add objects, add a + b.
        print(value['a'])
        yield value['a']+value['b']


async def send_value() -> None:
    for _ in range(100):
        print(await adding.ask(Add(a=4, b=random.randrange(100))))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_value())
