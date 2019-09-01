import faust

app = faust.App(
    'page_views',
    broker='kafka://localhost:9092',
    topic_partitions=4,
)

# model


class PageView(faust.Record):
    id: str
    user: str


# define topc
page_view_topic = app.topic('page_views', value_type=PageView)

# define Table(similar to dict)
page_views = app.Table('page_views', default=int)

# input stream
@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        page_views[view.id] += 1

# start worker
# faust -A parse worker -l info
# send data
# faust -A parse send page_views '{"id": "foo", "user": "bar"}'
# print key
# sudo /home/kafka/kafka/bin/kafka-console-consumer.sh --topic page_views-page_views-changelog --bootstrap-server localhost:9092 --property print.key=True --from-beginning