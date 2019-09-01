import rx
import asyncio
from rx import operators
import threading
from rx.scheduler.eventloop import AsyncIOScheduler

loop = asyncio.get_event_loop()
asyncio_scheduler = AsyncIOScheduler(loop)
numbers = rx.from_([1,2,3,4], scheduler=asyncio_scheduler)

subscription = numbers \
    .pipe(
    rx.operators.map(lambda i: i*2), \
    rx.operators.map(lambda i: "number is: {}".format(i))) \
    .subscribe(
        on_next = lambda i: print("on_next({}) {}"
            .format(threading.get_ident(), i)),
        on_error = lambda e: print("on_error({}): {}"
            .format(threading.get_ident(), e)),
        on_completed = lambda: print("on_completed({})"
            .format(threading.get_ident()))
)

print("starting event ")
loop.run_forever()
loop.close()