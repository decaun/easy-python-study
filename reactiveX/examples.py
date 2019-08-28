import rx

# Observable.of(*args, **kwargs)
numbers = rx.of(1, 2, 3, 4)
numbers.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# import rx

def create_numbers_observable(*args):
    return rx.of(*args)

create_numbers_observable(1, 2, 3, 4).subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# Observable.just(value, scheduler=None)
import rx

number = rx.just(1)
number.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# Observable.range(start, count, scheduler=None)
import rx

numbers = rx.range(1, 4)
numbers.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

import rx

numbers = rx.from_(range(1, 5, 2))
numbers.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# Observable.repeat(value=None, repeat_count=None, scheduler=None)
# Observable.repeat(self, repeat_count=None)
import rx
ones = rx.repeat_value(1, 5)
ones.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

import rx
from rx import operators
numbers = rx.from_([1,2,3])
numbers.pipe(rx.operators.repeat(3)).subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# Observable.empty() => empty obvervable
# Observable.never() => never emits
# Observable.throw(exception, scheduler=None) =>emits error

import rx
exception = rx.throw(NotImplementedError("I do nothing"))
exception.subscribe(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
    )

# Observable.timer(duetime, period=None, scheduler=None) => emit regarding time
import rx
import datetime

print("starting at {}".format(datetime.datetime.now()))
one_shot = rx.timer(1000)
one_shot.subscribe(
        on_next=lambda i: print("tick {} at {}".format(
            i, datetime.datetime.now())),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
)

# Observable.interval(period, scheduler=None) => emits in intervals
import rx
import datetime

ticks = rx.interval(1000)
ticks.subscribe(
        on_next=lambda i: print("tick {} at {}".format(
            i, datetime.datetime.now())),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed")
)

# Observable.from_callback(func, selector=None) => higher order function(synchronous)

import rx

def foo(what, handler):
    print("foo: {}".format(what))
    handler("hello " + what)

callback = rx.from_callback(foo)
cbk_obs = callback("world")
print("subscribing...")
cbk_obs.subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)

# Observable.create(subscribe)

import rx

def on_subscribe(observer,scheduler):
    observer.on_next(1)
    observer.on_next(2)
    observer.on_next(3)    
    observer.on_completed()

numbers = rx.create(on_subscribe)
numbers.subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)

import rx
def sum_even(source):
    def on_subscribe(observer,scheduler):
        accumulator = 0
        def on_next(i):
            nonlocal accumulator
            if i % 2 == 0:
                accumulator += i
            else:
                observer.on_next(accumulator)
                accumulator = i

        def on_error(e):
            observer.on_error()

        def on_completed():
            nonlocal accumulator            
            observer.on_next(accumulator)
            observer.on_completed()

        source.subscribe(on_next, on_error, on_completed)

    return rx.create(on_subscribe)

numbers = rx.from_([2,2,4,5,2])
sum_even(numbers).subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)