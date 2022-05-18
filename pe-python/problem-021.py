 # To time speed of the program.
from time import time

def sum_divisors(n):
    ''' Calculate the sum of proper divisors of an integer.
    
    Args:
        n: positive integer whose proper divisors we want to take the some of
    
    Returns:
        the sum of proper divisors of n.
    '''
    
    sm = 0
    for i in range(1, n):
        if (n % i) == 0:
            sm += i
    return sm

def amicable(a):
    ''' Checks if the input is an amicable number.
    
    Args:

        a: positive integer we want to check for amicability. If it is amicable, then sum_divisors(a) would be
            its amicable pair.
       
    Returns:
        Boolean True if the input is an amicable number and False if it is not an amicable number.
    '''
    
    # The amicability conditions are: d(a) = b, d(b) = a where d is the function giving the number of
    # divisors and then the other condition is a != b. These two conditions reduce to d(d(a)) = a and d(a) != a.
    return (sum_divisors(sum_divisors(a)) == a and sum_divisors(a) != a)

def sum_amicable(upper_bound):
    ''' Calculate the sum of amicable numbers below the given upper bound.
    
    Args:
        upper_bound: upperbound for the amicable number considerations; must be a positive number.
    
    Returns:
        the sum of all amicable numbers below (upper_bound).

    Raises:
        AssertionError when the input is not greater than zero.
    '''
    
    assert(upper_bound > 0)
    sm = 0
    for i in range(1, upper_bound):
        if amicable(i):
            sm += i
    return sm

if __name__ == "__main__":
    up_bnd = int(input("Please input the upperbound for the amicable numbers to be considered: "))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    sm_amic = sum_amicable(up_bnd)
    print(f'The sum of amicable numbers below {up_bnd} is: {sm_amic}')
    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end-strt}s')