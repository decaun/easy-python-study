from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    params = request.rel_url.query
    return web.Response(text="Hello, world " +
                        (params['id'] if request.rel_url.query else ""))

app = web.Application()
app.add_routes(routes)
web.run_app(app)
