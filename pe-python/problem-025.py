 # To time speed of the program.
from time import time

def fibonacci(n): 
    ''' Calculate the (n)th Fibonacci number.

    Args:
        n: the index/ardinal number of the required Fibonacci number.
    
    Returns:
        The nth Fibonacci number where n is the input.
    '''

    f1 = 1
    f2 = 1
    for i in range(3, n+1):
        f1, f2 = f2, f1 + f2
    return f2


def first_fib_m_digits(num_digits):
    ''' Calculate The first Fibonacci number, and its index/cardinal, 
            containing a number of digits greater than or equal to than a given input.

    Args:
        digits_max: The number of digits of the required Fibonacci number.

    Returns:
        The first Fibonacci number, and its index/cardinal, containing a number of digits  greater than
            or equal to the given input.
    '''
    n = 1
    while (len(str(fibonacci(n))) < num_digits):
        n += 1
    return fibonacci(n), n


if __name__ == "__main__":
    N = int(input('Enter number of digits required: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()

    fib, ind = first_fib_m_digits(N)

    end = time()

    print(f"The index/cardinal of the first Fibonacci number with {N} digits is: {ind}")
    print('------------------------------------------------\n------------------------------------------------')
    print(f"Time taken: {end - strt} s")

