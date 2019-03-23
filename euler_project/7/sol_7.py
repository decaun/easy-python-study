"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def search_for_next_prime(current=3):
    next_prime=None
    while next_prime==None:
        for i in range(2,current):
            if current%i!=0:
                next_prime=current
            else:
                break
        current+=1
    return next_prime

def prime(order=6):
    prime_counter=0
    previous_prime=search_for_next_prime(order-1)
    current_prime=search_for_next_prime(order)
    _next_prime=search_for_next_prime(previous_prime)
    while _next_prime == previous_prime:
        _next_prime=search_for_next_prime(previous_prime+prime_counter)        
        prime_counter+=1
    return current_prime

if __name__=="__main__":
    print(prime(1))
    print(search_for_next_prime(8))
