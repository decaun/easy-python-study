"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
<<<<<<< HEAD
def search_for_next_prime(current=1):
=======
def search_for_next_prime(current=3):
>>>>>>> refs/remotes/origin/master
    next_prime=None
    while next_prime==None:
<<<<<<< HEAD
        broken=None
        current+=1
        
=======
>>>>>>> refs/remotes/origin/master
        for i in range(2,current):
            if current%i==0:
                broken=True
                break
<<<<<<< HEAD
                
        if broken==None:
            next_prime=current
        
=======
        current+=1
>>>>>>> refs/remotes/origin/master
    return next_prime

<<<<<<< HEAD
def prime(order=1):
    prime_counter=1
    prime=search_for_next_prime()  
    while prime_counter < order:
        prime=search_for_next_prime(prime)
        prime_counter+=1
        
    return prime
=======
def prime(order=6):
    prime_counter=0
    previous_prime=search_for_next_prime(order-1)
    current_prime=search_for_next_prime(order)
    _next_prime=search_for_next_prime(previous_prime)
    while _next_prime == previous_prime:
        _next_prime=search_for_next_prime(previous_prime+prime_counter)        
        prime_counter+=1
    return current_prime
>>>>>>> refs/remotes/origin/master

if __name__=="__main__":
<<<<<<< HEAD
    print(prime(10001))
=======
    print(prime(1))
    print(search_for_next_prime(8))
>>>>>>> refs/remotes/origin/master
