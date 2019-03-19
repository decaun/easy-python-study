def multiples_3_5(var=9):
    result=0
    while var > 2:
        if var%3==0 or var%5==0:
            result=result+var
        var-=1
    return result
    
print (multiples_3_5(999))