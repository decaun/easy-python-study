import ssl
import pathlib
import asyncio
import websockets


async def response(websocket, path):
    message = await websocket.recv()
    print(f"Got message from client: {message}")
    await websocket.send("ACK")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(pathlib.Path(__file__).with_name('mycert.crt'),keyfile = pathlib.Path(__file__).with_name('mykey.key'))

start_server = websockets.serve(response, 'localhost', 1234, ssl=ssl_context)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
