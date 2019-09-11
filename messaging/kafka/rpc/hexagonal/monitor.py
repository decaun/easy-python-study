import faust

app = faust.App(
    'monitor',
    # web_enabled=False,
    web_port=1231
)


class Add(faust.Record):
    a: int
    b: int


stream = app.topic('adding', value_type=Add)


@app.agent(stream)
async def monitor(events):
    async for event in events:
        print(event)

# start worker
# faust -A hello_world worker -l info
# send message
# faust -A hello_world send @greet "Hello Faust"
# faust -A hello_world send greetings "Hello Kafka topic"
# use to launch http://supervisord.org/
# faust -A hello_world send greetings '{"id": "foo", "user": "bar"}'

if __name__ == '__main__':
    app.main()
# python monitor worker --without-web
