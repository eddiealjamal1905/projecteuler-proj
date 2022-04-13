# To time speed of the program.
from time import time

def largest_palindrome_mult_of_2_numbers(num_digits):
    '''Find the largest palindrome made by multiplying two number containing any number of digits

    Args:
        num_digits - the number of digits in each of the two numbers
        
    Returns:
        largest palindrome made by mutliply two numbers.
    '''

    palin = 0 
    for i in range(1, 10**num_digits):
        for j in range(1, 10**num_digits):
            if (list(str(i*j)) == list(str(i*j))[::-1]) and (i*j > palin):
                palin = i*j
    return palin

# Run the search for the largest palindrome as a product of two numbers.
if __name__ == '__main__':
    num_digits = int(input('Enter the number of digits (positive integer) in the numbers you multiply for the palindrome: '))
    print('-----------------------------------------\n-----------------------------------------')

    strt = time()
    m = largest_palindrome_mult_of_2_numbers(num_digits)
    print(f'The largest palindrome number that is the product of two {num_digits} digit numbers is: {m}.')
    end = time()
    print('-----------------------------------------\n-----------------------------------------')
    print(f'Time taken {end-strt} s')