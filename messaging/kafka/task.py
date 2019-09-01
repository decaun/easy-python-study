# faust -A task worker -l info --web-port 1234
# python task.py produce

import faust
app = faust.App('myapp2', broker='kafka://')


class AddOperation(faust.Record):

    x: int
    y: int


@app.agent()
async def add(stream):
    async for op in stream:
        yield op.x + op.y


@app.command()
async def produce():
    await add.send(value=AddOperation(2, 2))

if __name__ == '__main__':
    app.main()
