# For factorial function.
import math
# To time speed of the program.
from time import time

# For imporvement: Check divisibility of prime factors first.


def smallest_number_divisible_by_every_number(upper_bound):
    '''We calculate the smallest number that divides all integers between 1 and and some inclusive upper bound.
    
    Args:
        upper_bound: The inclusive upper bound with smaller numbers to be considered as the divisors for our 
            desired result.
    
    Returns:
        Smallest number that divides all integers between 1 and the upper bound inclusive.

    Raises:
        ValueError: If the upperbound is not greater than 1.
    '''

    if (not upper_bound > 1):
        raise ValueError(f"The chosen upper bound must be a positive integer greater than 1.")
    for i in range(1, math.factorial(upper_bound)):
        if (i >= upper_bound):
            if all(i % x == 0 for x in range(1,upper_bound + 1)):
                break
    return i

if __name__ == "__main__":
    up_bound = int(input('Please enter the desired positive integer greater than 1 as upper bound (inclusive) for divisibility: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    smallest_divisible = smallest_number_divisible_by_every_number(up_bound)
    end = time()
    print(f"The smallest number divisible by every positive number less than or equal to {up_bound} is: {smallest_divisible}")
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end-strt} s')