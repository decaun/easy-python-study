from rx import operators
import rx


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)

zen_quotes = get_quotes()

rx.from_(zen_quotes, scheduler=None).pipe(\
    rx.operators.filter(lambda q: len(q[1]) > 0)\
        ).subscribe(lambda value: print(f"Received: {value[0]} - {value[1]}"))

