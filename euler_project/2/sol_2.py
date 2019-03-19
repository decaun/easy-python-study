def fibonacci(limit=10):
    a,b=0,1
    while b<limit:
        a,b=b,a+b
        yield b

fib=fibonacci(4000000)
sum=0
for i in fib:
    if i%2==0:
        sum+=i

print(sum)

fib=None
fib=fibonacci(40)
print(list(fib))
"""
sum=0
x=1
f=fibonacci(x)
while f<4000000:
    f=fibonacci(x)
    if f%2==0:
        sum+=f
        x+=1

print(sum)
"""