"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples_3_5(var=9):
    result=0
    while var > 2:
        if var%3==0 or var%5==0:
            result=result+var
        var-=1
    return result
    
print (multiples_3_5(999))