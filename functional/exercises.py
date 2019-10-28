## ex1 '__code__'
def example(a, b, **kw):
    return a*b

type(example)
example.__code__.co_varnames
example.__code__.co_argcount
example.__code__.co_freevars
dir(example.__code__)

## ex2 'isprime'
import math
isprime=lambda n:not any(n%p==0 for p in range(2,int(math.sqrt(n))+1))
isprime(2)
isprime(4)

## ex3 Strategy pattern
import collections
class Mersenne1(collections.Callable):
    def __init__(self, algorithm):
        self.pow2= algorithm
    def __call__(self, arg):
        return self.pow2(arg)-1

def shifty(b):
    return 1 << b
def multy(b):
    if b == 0: return 1
    return 2*multy(b-1)
def faster(b):
    if b == 0: return 1
    if b%2 == 1: return 2*faster(b-1)
    t= faster(b//2)
    return t*t

m1s= Mersenne1(shifty)
m1m= Mersenne1(multy)
m1f= Mersenne1(faster)
