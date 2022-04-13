# To time speed of the program.
from time import time

def sum_multiples(factor1, factor2, upper_bound = 1000):
    '''Find the sum of multiples of either two numbers under some upper bound.

    Args:
        factor1: First integer whose multiples will be considered.
        factor2: Second integer whose multiples will be considered.
        upper_bound: The upper bound cutoff for multiples of factor1 and factor2 to be considered.
                      default: 1000.

    Returns:
        s: Sum of the multiples below upper_bound.
        cnt: The count of multiples of either factor1 or factor2 below upper_bound.
    '''

    cnt = 0
    s = 0
    for i in range(1, upper_bound):
        if i % factor1 == 0 or i % factor2 == 0:
            s += i
            cnt += 1
    return s, cnt

# Run the sum and count of factors.
if __name__ == "__main__":

    f1, f2 = tuple(map(int,input('Enter the two positive integer factors separated by a space: ').split()))
    upbnd = int(input('Enter a postive integer upperbound for the search of multiples: '))
    print('-------------------------------------------\n-------------------------------------------')

    strt = time()
    s, cnt = sum_multiples(f1, f2, upbnd)
    print(f"sum of multiples of {f1} or {f2} below {upbnd} is: {s}.")
    print(f"Number of multiples of {f1} or {f2} below {upbnd} is: {cnt}.")

    end = time()
    print('-----------------------------------------\n-----------------------------------------')
    print(f'Time taken: {end - strt} s')