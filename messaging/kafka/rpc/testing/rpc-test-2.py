#!/usr/bin/env python
from typing import AsyncIterable
import faust
from faust import StreamT


app = faust.App('RPCTest2')
topic = app.topic('RPC__test_2')


@app.agent(topic)
async def rpc_call(stream: StreamT[float]) -> AsyncIterable[float]:
    async for value in stream:
        print("rpc-test-2 rpc_call value: {}".format(value))
        yield value * 20


if __name__ == '__main__':
    app.main()