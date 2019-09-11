from aiohttp import web
import aiohttp
import asyncio
import random
import faust
# from tornado.platform.asyncio import AsyncIOMainLoop
# import uvloop

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
    wait = random.randrange(0, 10)
    timeout = aiohttp.ClientTimeout(total=5, connect=1,
                                    sock_connect=1, sock_read=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        reply = str(await adding.ask(Add(a=4, b=wait)))
        # await asyncio.sleep(wait)
        return web.Response(text="Hello, world " + reply +
                            (params['id'] if request.rel_url.query else ""))
# uvloop not stable for handling requests but
# better to use it for performing requests


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == "__main__":
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    # AsyncIOMainLoop().install()

    # 启动 Server
    try:
        main()
    except Exception as e:
        print(e)
