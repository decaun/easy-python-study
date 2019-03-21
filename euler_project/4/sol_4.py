x=list("100001")
assert x[-1] == x[0]
assert x[-2] == x[1]
assert x[-3] == x[2]

def palindrome_2():
    result=[]
    a,b=999,998
    while a>100:
        b=998
        a-=1
        while b>100:
            try:
                x=list(str(a*b))
                assert x[-1] == x[0]
                assert x[-2] == x[1]
                assert x[-3] == x[2]
                result.append(int("".join(x)))
            except:
                pass
            b-=1
    return max(result)

print(palindrome_2())