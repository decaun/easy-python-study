from aiohttp import web
import asyncio
import uvloop
import random
import faust
import random


class Add(faust.Record):
    a: int
    b: int


rpc_app = faust.App('RPCClientApp', reply_create_topic=True, broker_max_poll_records=1000,
                    stream_publish_on_commit=True,
                    stream_buffer_maxsize=1000, broker_commit_interval=0.001,
                    broker_commit_every=0.001)
topic = rpc_app.topic('adding', value_type=Add)


@rpc_app.agent(topic)
async def adding(stream):
    async for value in stream:
        # here we receive Add objects, add a + b.
        print(value['a'])
        yield value['a']+value['b']


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    params = request.rel_url.query
    # await asyncio.sleep(random.randrange(0, 10))
    resp = 
    return web.Response(text="Hello, world " + str(await adding.ask(Add(a=4, b=random.randrange(100)))) +
                        (params['id'] if request.rel_url.query else ""))

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = web.Application()
app.add_routes(routes)
web.run_app(app)
