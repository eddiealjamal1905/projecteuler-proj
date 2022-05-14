 # To time speed of the program.
from time import time

def sum_digits_power(base, exp):
    ''' Calculates the sum of digits of the number (base)^(exp).
    
    Args:
        base: base number of the power.
        exp: exponent of the power.
       
    Returns:
        Rhe sum of the digits in (base)^(exp).
    '''

    number = base**exp

    return sum(map(int, list(str(number))))

if __name__ == '__main__':
    base = int(input('Enter the desired base number: '))
    exp = int(input('Enter the desired exponent: '))
    print('------------------------------------------------\n------------------------------------------------')

    strt = time()
    sm = sum_digits_power(base, exp)
    end = time()
    print(f'The sum of digits of {base}^{exp} is: {sm}')
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time Taken: {end-strt} s')