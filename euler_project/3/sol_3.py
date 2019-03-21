def find_div(var):
    div=2
    result=[]
    while div<=var:
        if var%div==0:
            var/=div
            result.append(div)
        div+=1
    return result

print(find_div(600851475143))

