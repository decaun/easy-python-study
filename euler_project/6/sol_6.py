def sum_of_squares(last):
    if last==1:
        return 1
    else:
        return last**2 + sum_of_squares(last-1)
    
def square_of_sum(last):
    for i in range(1,last):
        last+=i
    return last**2

def sos_diff(last):
    return abs(square_of_sum(last)-sum_of_squares(last))

print(sos_diff(100))