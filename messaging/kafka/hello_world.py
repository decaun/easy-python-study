import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)

# start worker
# faust -A hello_world worker -l info
# send message
# faust -A hello_world send @greet "Hello Faust"
# faust -A hello_world send greetings "Hello Kafka topic"
# use to launch http://supervisord.org/
# faust -A hello_world send greetings '{"id": "foo", "user": "bar"}'