"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def search_for_next_prime(current=2):
    next_prime=None
    while next_prime==None:
        current+=1
        
        for i in range(2,current):
            if current%i==0:
                current+=1
            
        next_prime=current
        
    return next_prime


def prime(order=1):
    prime_counter=1
    
    prime=search_for_next_prime()  
    while prime_counter < order:
        prime=search_for_next_prime(prime)
        prime_counter+=1
        
    return prime

print(prime(10000))