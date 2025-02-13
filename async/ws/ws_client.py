import asyncio
import websockets


async def message():
    async with websockets.connect("ws://localhost:1234") as socket:
        msg = input("Message")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
