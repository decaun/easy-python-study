from aiohttp import web
import asyncio
import random

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    params = request.rel_url.query
    # await asyncio.sleep(random.randrange(0, 10))
    return web.Response(text="Hello, world " +
                        (params['id'] if request.rel_url.query else ""))

app = web.Application()
app.add_routes(routes)
web.run_app(app)
