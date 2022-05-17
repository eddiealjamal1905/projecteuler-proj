 # To time speed of the program.
from time import time
from math import factorial


def factorial_sum_digits(n):
    ''' Calculate the sum of digits that results from taking the factorial of the input.
    
    Args:
        n: non-negative integer for which the sum of digits in factorial(n) will be calculated.
    
    Returns: 
        the sum of digits of (n!)
    '''

    assert(n >= 0)
    fact_list = map(int,list(str(factorial(n))))
    return sum(fact_list)

if __name__ == "__main__":
    N = int(input('Please input the factorial number: '))
    print('------------------------------------------------\n------------------------------------------------')

    strt = time()
    sum_digits = factorial_sum_digits(N)
    print(f"The sum of digits in {N}! is: {sum_digits}")
    print('------------------------------------------------\n------------------------------------------------')

    end = time()
    print(f'Time Taken: {end-strt}s')