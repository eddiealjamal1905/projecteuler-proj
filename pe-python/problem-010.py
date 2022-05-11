 # To time speed of the program.
from time import time

def isPrime(n):
    '''Check if a mumber is a prime number usig the 6k +/- 1 optimization described above.
    Args:
        n: The number that we check if it is prime or not.

    Returns:
        Boolean True if the input is [rime, otherwise returns False.
    '''

    if (n <= 1):
        return False
    if (n <= 3):
        return True
    
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
        
    return True

def primes_under(upper_bound):
    '''Finding the primes under given upper bound and their sum.

    Args:
        upper_bound: The maximum (exclusive) value under which we consider the prime numbers.

    Returns:
        Tuple with first element of tuple being a list of the prime numbers under the upper bound,
            and the second being the sum of these prime numbers. 
    '''

    # We put two initially in primes_list because we want the loop to go over only odd numbers.
    primes_list = [2]
    for i in range(3, upper_bound, 2):
        if isPrime(i):
            primes_list.append(i)
    return primes_list, sum(primes_list)

if __name__ == "__main__":
    up_bound = int(input('Please enter the desired upper bound for the primes: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    _, s = primes_under(up_bound)
    print(f'The sum of primes below {up_bound} is: {s}')
    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end-strt} s')