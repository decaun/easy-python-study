from aiohttp import web
import asyncio
import uvloop
import random
import faust


class Add(faust.Record):
    a: int
    b: int


rpc_app = faust.App('RPCClientApp', reply_create_topic=False, broker_max_poll_records=1000,
                    stream_publish_on_commit=True,
                    stream_buffer_maxsize=1000, broker_commit_interval=0.001,
                    broker_commit_every=0.001)
topic = rpc_app.topic('adding', value_type=Add)


@rpc_app.agent(topic)
async def adding(stream):
    pass


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    params = request.rel_url.query
    wait=random.randrange(0, 10)
    reply = str(await adding.ask(Add(a=4, b=wait)))
    await asyncio.sleep(wait)
    return web.Response(text="Hello, world " + reply +
                        (params['id'] if request.rel_url.query else ""))

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.add_routes(routes)
web.run_app(app)
