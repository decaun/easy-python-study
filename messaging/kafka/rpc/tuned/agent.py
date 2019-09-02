# python agent.py worker --without-web

import faust

# The model describes the data sent to our agent,
# We will use a JSON serialized dictionary
# with two integer fields: a, and b.


class Add(faust.Record):
    a: int
    b: int


# Next, we create the Faust application object that
# configures our environment.
app = faust.App('agent-example', reply_create_topic=True,
                stream_buffer_maxsize=64, broker_commit_interval=0.001,
                broker_commit_every=0.001)
# The Kafka topic used by our agent is named 'adding',
# and we specify that the values in this topic are of the Add model.
# (you can also specify the key_type if your topic uses keys).
topic = app.topic('adding', value_type=Add)


@app.agent(topic)
async def adding(stream):
    async for value in stream:
        # here we receive Add objects, add a + b.
        print(value['a'])
        yield value['a']+value['b']

if __name__ == '__main__':
    app.main()
