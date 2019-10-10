from greeter_pb2 import HelloRequest, HelloReply
from greeter_grpc import GreeterServicer
from purerpc import Server


class Greeter(GreeterServicer):
    async def SayHello(self, message):
        return HelloReply(message="Hello, " + message.name)

    async def SayHelloToMany(self, input_messages):
        async for message in input_messages:
            yield HelloReply(message=f"Hello, {message.name}")


server = Server(50055)
server.add_service(Greeter().service)
# backend can also be one of: "uvloop", "curio", "trio"
server.serve(backend="asyncio")
