# To time speed of the program.
from time import time
# For square root function, sqrt.
import numpy as np


def prime_factors(n):
    '''Return a list of prime factors of an integer.
    
    Args:
        n: A positive integer whose prime factors will be listed.
    
    Returns:
        A list of of prime factors of the input.
    '''

    primelst = set()
    while n % 2 == 0:
        primelst.add(2)
        n = int(n/2)
    for i in range(3, int(np.sqrt(n)) + 1, 2): # step = 2 since n is odd now.
        while n % i == 0:
            primelst.add(i)
            n = int(n/i)
    
    if n > 2:
        primelst.add(int(n))
    return list(primelst)


# Run the search for the largest prime factor.
if __name__ == "__main__":
    num = int(input('Enter the positive integer for which we want to compute the largest prime factor: '))
    print('--------------------------------------\n--------------------------------------')

    strt = time()

    primelist = prime_factors(num)

    print(f"The largest prime factor of {num} is: {max(primelist)}.")
    print(f"The set of prime factors of {num} is: {sorted(primelist)}.")
    end = time()
    print('-----------------------------------------\n-----------------------------------------')
    print(f'Time taken: {end-strt} s')