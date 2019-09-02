#!/usr/bin/env python
'''
python rpc-test-1.py worker --without-web
python rpc-test-2.py worker --without-web
python rpc-test-client.py worker --without-web
'''
from typing import AsyncIterable
import faust
from faust import StreamT

# Main App.
app = faust.App('RPCTestClient')
app_topic = app.topic('RPC__test_app')

# RPC Client App.
rpc_app = faust.App('RPCClientApp', reply_create_topic=True)
rpc_topic_1 = rpc_app.topic('RPC__test_1')
rpc_topic_2 = rpc_app.topic('RPC__test_2')

# RPC 'RPC__test_1' topic client agent.
@rpc_app.agent(rpc_topic_1)
async def rpc_test_1_noop(stream: StreamT[float]) -> AsyncIterable[float]:
    # This is never called. Only used to create RPC client agent.
    async for value in stream:
        print("rpc-test-client rpc_test_1_noop value: {}".format(value))
        yield 3.14

# RPC 'RPC__test_2' topic client agent.
@rpc_app.agent(rpc_topic_2)
async def rpc_test_2_noop(stream: StreamT[float]) -> AsyncIterable[float]:
    # This is never called. Only used to create RPC client agent.
    async for value in stream:
        print("rpc-test-client rpc_test_2_noop value: {}".format(value))
        yield 3.14

# Main App agent that makes RPCs to 'RPC__test_1' and 'RPC__test_2'.
@app.agent(app_topic)
async def process(stream: StreamT[float]) -> None:
    async for value in stream:
        print("rpc-test-client process value: {}".format(value))

        res = await rpc_test_1_noop.ask(value=value)

        print("rpc-test-client process res: {}".format(res))

        res = await rpc_test_2_noop.ask(value=res)

        print("rpc-test-client process res: {}".format(res))

# Test sending value to main Apps 'RPC__test_app' topic.
@app.timer(interval=5)
async def _sender() -> None:
    value = 5
    print("rpc-test-client _sender value: {}".format(value))
    await app_topic.send(value=value)


# Start RPC Client App in client mode.
@app.task
async def on_startup(app):
    print('STARTING UP: %r' % (app,))
    await rpc_app.start_client()
    print('START UP COMPLETED: %r' % (app,))


# Start main App.
if __name__ == '__main__':
    app.main()