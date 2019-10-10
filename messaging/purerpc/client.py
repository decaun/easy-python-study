import anyio
import purerpc
from greeter_pb2 import HelloRequest, HelloReply
from greeter_grpc import GreeterStub


async def gen():
    for i in range(5):
        yield HelloRequest(name=str(i))


async def main():
    async with purerpc.insecure_channel("localhost", 50055) as channel:
        stub = GreeterStub(channel)
        reply = await stub.SayHello(HelloRequest(name="World"))
        print(reply.message)

        async for reply in stub.SayHelloToMany(gen()):
            print(reply.message)


if __name__ == "__main__":
    # backend can also be one of: "uvloop", "curio", "trio"
    anyio.run(main, backend="asyncio")
