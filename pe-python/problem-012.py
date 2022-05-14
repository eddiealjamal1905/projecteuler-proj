 # To time speed of the program.
from time import time
import numpy as np

def nth_triangle_num(n):
    ''' Calculate the nth triangle number. The nth triangle number
            is the sum of the first 7 natural numbers.

    Args:
        n - Index/cardinal of required traingle number.

    Returns:
        nth triangle number.
    '''

    assert(isinstance(n, int) and n > 0)

    return sum(range(1,n+1))

def num_divisors(n):
    ''' Calculate the number of divisors of a given positive integer.

    Args:
        n - positive integer for which we are calculating the number of divisors.

    Returns:
        Number of divisors of the argument n.    
    '''

    assert(isinstance(n, int))
    i = 1
    num_divs = 0
    while (i <= np.sqrt(n)):
        if n % i == 0:
            num_divs += 1
        i += 1
    # divisors come in pairs, one of the pairs is less than sqrt(n) and the other greater except
    # when it is a perfect square
    num_divs = (2*num_divs - 1) if (n/np.sqrt(n) == np.sqrt(n))  else 2*num_divs 
    
    return num_divs

def first_triangle_num_m_divisors(m):
    ''' Calculate the first triangle number that has a number of divisors that is greater than or equal to 
            a given input and also give the index/cadinal of that triangle number and the number of its divisors.
        
    Args:
        m: the given lower bound for the number of diviosors that the triangle number we are searching
                for is required to have.
    
    Returns:
        A tuple of three entries where the first entry is the first triangle number that has a number
            of divisors greater than or equal to the given upper bound; the second entry is 
            the index/cardinal of that triangle number; the third entry is the number of divisors
            that triangle number has.
    '''
    
    # Maybe we can find a better starting point for n, to skip checking all the numbers that we know don't have
    # more than m divisors. For that we need to get an upper bound for the number of divisors of a number and 
    # invert the saturation of this inequality at m. So we can find the highest number for which the number of
    # divisors is known to be less than m.
    n = 1
    num_divs = 1 
    while (num_divs < m):
        n += 1
        triang = nth_triangle_num(n)
        num_divs = num_divisors(triang)
    
    return (triang, n, num_divs)

if __name__ == "__main__":
    N = int(input('Enter desired number of divisors: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    num_divisor = 0
    num, tri_ind, numdivs = first_triangle_num_m_divisors(N)
    print(f'The value of the first triangle number with over {N} divisors is: {num}.\n It is the {tri_ind}th triangle number and it has {numdivs} divisors') 
    print('------------------------------------------------\n------------------------------------------------')
    end = time()
    print('Time taken:',end-strt)