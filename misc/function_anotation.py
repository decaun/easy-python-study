from typing import no_type_check

@no_type_check
def foo(a:'ananas', b: {'some ' 'set'}) -> 'oy':
    return a

print(foo.__annotations__.get('return'))
