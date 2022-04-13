# To time speed of the program.
from time import time

# An iterative Fibonacci because it could take in larger inputs than the recursive version and it is faster.
def fib(n):
    '''Produce the (n)th Fibonacci number starting with 1,2.
    
    Args: 
        n - A positive integer indicating the desired Fibonacci index.

    Returns:
        nth Fibonacci number.

    Raises:
        ValueError: If input, n, is not positive.
        TypeError: If input, n, is not an integer.
    '''

    if (n < 0):
        raise ValueError(f"Fibonacci index entered must be a positive, not {n}.")
    if (not isinstance(n, int)):
        raise TypeError(f"Fibonacci index entered must be an integer, not {n}.")

    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def sum_even_fib(upper_bound):
    '''Return the sum of even Fibonacci numbers under desired upper bound.
    
    Args:
        upper_bound: An integer indicating the desired upper_bound for the sum of Fibonacci numbers.

    Retruns:
        Sum of all Fibonacci numbers that are strictly less than the upper bound.
    '''

    a, b = 0, 1
    s = 0
    i = 1
    x = fib(i)
    while x < (upper_bound + 1):
        if x % 2 == 0:
            s += x
        i += 1
        x = fib(i)
    return s

# Run the sum of even Fibonacci numbers.
if __name__ == '__main__':

    upbnd = float(input('Enter the desired positive upper bound: '))
    print('-----------------------------------------\n-----------------------------------------')

    strt = time()

    s = sum_even_fib(upbnd)
    print(f"The sum of the even numbers in fibonacci sequence below {upbnd}: {s}.")
    end = time()
    print('-----------------------------------------\n-----------------------------------------')
    print(f'Time taken: {end - strt} s')