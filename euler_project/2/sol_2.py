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
