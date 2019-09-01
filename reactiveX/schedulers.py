# names are self explanatory

from rx.scheduler import NewThreadScheduler
from rx.scheduler import ThreadPoolScheduler
from rx.scheduler.eventloop import AsyncIOScheduler

import rx
from rx import operators
import threading
from rx.scheduler import NewThreadScheduler

new_thread_scheduler = NewThreadScheduler()
numbers = rx.from_([1,2,3,4], scheduler=new_thread_scheduler)

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
print("main({})".format(threading.get_ident()))


# some errors happen when trying to observe on different thread etc.
'''

import rx
from rx import operators
import threading
from rx.scheduler import ThreadPoolScheduler

threadpool_scheduler = ThreadPoolScheduler()
numbers = rx.from_([1,2,3,4])

subscription = numbers \
    .pipe(
    rx.operators.map(lambda i: i*2), \
    rx.operators.observe_on(threadpool_scheduler), \
    rx.operators.map(lambda i: "number is: {}".format(i))) \
    .subscribe(   
        on_next = lambda i: print("on_next({}) {}"
            .format(threading.get_ident(), i)),
        on_error = lambda e: print("on_error({}): {}"
            .format(threading.get_ident(), e)),
        on_completed = lambda: print("on_completed({})"
            .format(threading.get_ident()))
)
print("main({})".format(threading.get_ident()))

'''

# async scheduler without issue except left loop open
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