"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def search_for_next_prime(current=2):
    next_prime=None
    while next_prime==None:
        current+=1
        for i in range(2,current):
            if current%i!=0:
                next_prime=current
            else:
                break
    return next_prime


def prime(order=6):
    prime_counter=0
    previous_prime=None
    
    while prime_counter < order:
            
            if previous_prime==None:
                previous_prime=search_for_next_prime(previous_prime)
            else:
                prime_counter+=1

    return previous_prime


print(search_for_next_prime(13))