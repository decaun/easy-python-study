import rx
from rx import operators

numbers = rx.from_([1,2,3])
pub_numbers = numbers.pipe(rx.operators.publish())
# numbers regular observable
# pub_numbers > connectable observable
pub_numbers.connect()

pub_numbers.subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)

pub_numbers.subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)

# depends where bellow run inside code, @connect data is emitted from connectable observable.
# pub_numbers.connect()