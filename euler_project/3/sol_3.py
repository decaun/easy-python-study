"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def find_div(var):
    div=2
    result=[]

    while div<=var:
        if var%div==0:
            var/=div
            result.append(div)
        div+=1
    return result

if __name__=="__main__":
    print(max(find_div(600851475143)))

