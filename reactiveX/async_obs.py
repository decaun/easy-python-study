# not thread safe
import rx
import threading

def foo():
    print("foo from {}".format(threading.get_ident()))
    return 1

number = rx.start(foo)
print("subscribing...")
number.subscribe(
        on_next=lambda i: print("on_next: {} from {}".format(
            i, threading.get_ident())),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# thread safe
import rx
import asyncio
import threading
from rx.scheduler.eventloop import AsyncIOScheduler

def foo():
    print("foo from {}".format(threading.get_ident()))
    return 2


loop = asyncio.get_event_loop()
scheduler = AsyncIOScheduler(loop)
done = loop.create_future()

number = rx.start(foo, scheduler=scheduler)
print("subscribing...")
number.subscribe(
    lambda i: print("on_next: {} from {}".format(
        i, threading.get_ident())),
    lambda e: print("on_error: {}".format(e)),
    lambda: done.set_result(0)
)

print("staring mainloop from {}".format(threading.get_ident()))
loop.run_until_complete(done)
loop.close()

# future
import asyncio
import rx


async def foo(future):
    await asyncio.sleep(0.0000001)
    future.set_result(2)


loop = asyncio.get_event_loop()
done = loop.create_future()
asyncio.ensure_future(foo(done))

number = rx.from_future(done)
print("subscribing...")
number.subscribe(
    lambda i: print("on_next: {}".format(i)),
    lambda e: print("on_error: {}".format(e)),
    lambda: print("on_completed")
)

print("starting mainloop")
loop.run_until_complete(done)
loop.close()