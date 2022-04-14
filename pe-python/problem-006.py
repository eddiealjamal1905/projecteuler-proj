# To time speed of the program.
from time import time


def sum_square_difference(upper_bound):
    '''We calculate the difference between the square of a sum of integers and the sum of squares of integers
        up to some upperbound.
        
    Args:
        upper_bound: Maximum positive integer at which to end the sum of integers and the sum of the squares.
        
    Returns:
        The difference between the square of the sum of integers below the upperbound and the sum of squares of the
            same integers.
    '''

    square_sum = sum(range(1,upper_bound + 1))
    sum_of_squares = sum([x**2 for x in range(1, upper_bound + 1)])

    return (square_sum**2 - sum_of_squares)


if __name__ == "__main__":
    upperbound = int(input('Enter desired upper bound for natural numbers: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()

    diff = sum_square_difference(upperbound)
    print(f'Difference between the square of the sum and the sum of squares of the first {upperbound} natural numbers is: {diff}')
    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end-strt} s')