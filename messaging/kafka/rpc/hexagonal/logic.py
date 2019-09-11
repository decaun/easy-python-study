# python logic.py worker --without-web

import faust

# The model describes the data sent to our agent,
# We will use a JSON serialized dictionary
# with two integer fields: a, and b.


class Add(faust.Record):
    a: int
    b: int


# Next, we create the Faust application object that
# configures our environment.
app = faust.App('agent-example', reply_create_topic=False, broker_max_poll_records=1000,
                stream_publish_on_commit=True,
                stream_buffer_maxsize=1000, broker_commit_interval=0.001,
                broker_commit_every=0.001)
# The Kafka topic used by our agent is named 'adding',
# and we specify that the values in this topic are of the Add model.
# (you can also specify the key_type if your topic uses keys).
topic = app.topic('adding', value_type=Add)


@app.agent(topic)
async def adding(stream):
    async for value in stream:
        # here we receive Add objects, add a + b.
        print(value['b'])
        yield value['b']

if __name__ == '__main__':
    app.main()
