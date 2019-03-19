def fibonacci(var):
    a,b=1,2
    for _ in range(1,var):
        a,b=b,a+b
        
    return a


sum=0
x=1
f=fibonacci(x)
while f<4000000:
    f=fibonacci(x)
    if f%2==0:
        sum+=f
        x+=1

print(sum)