import rx

numbers = rx.from_([1, 2, 3])
subscription = numbers.subscribe(
    on_next = lambda i: print("on_next {}".format(i)),
    on_error = lambda e: print("on_error: {}".format(e)),
    on_completed = lambda: print("on_completed")
)
subscription.dispose()

import rx

def on_subscribe(observer,scheduler):
    def dispose():
        print("disposing custom observable")

    observer.on_next(1)
    observer.on_next(2)
    observer.on_next(3) 
    observer.on_completed()
    return dispose

numbers = rx.create(on_subscribe)
subscription = numbers.subscribe(
    on_next = lambda i: print("on_next {}".format(i)),
    on_error = lambda e: print("on_error: {}".format(e)),
    on_completed = lambda: print("on_completed")
)
subscription.dispose()