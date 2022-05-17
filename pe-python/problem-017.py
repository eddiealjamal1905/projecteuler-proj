 # To time speed of the program.
from time import time

def count_letters(n):
    ''' Calculate the number of letters in written version of the input integer according to 
            British usage.

    Args:
        n: any integer between 1 and 1001 for which we will count the letters.
    
    Returns:
        The number of letters when the number n is written in English according to British usage.
    '''

    assert(n < 1001 and n > 0 and isinstance(n, int))
    d = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
         10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
         20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6,
         100: 10, 1000: 11}
    cnt = 0
    if 1 <= n <= 20:
        cnt += d[n]
    elif 20 < n < 100:
        tens = (n//10)*10
        ones = n - tens
        cnt += + d[tens] + d[ones]
    elif 100 <= n < 1000:
            hundreds = (n//100)
            tens = ((n-hundreds * 100)//10) * 10
            ones = (n - hundreds * 100 - tens)
            if ones == 0 and tens == 0:                            # No 'and' in 100, 200, etc...
                cnt += 7 + d[hundreds]
            elif tens < 20:
                cnt += d[hundreds] + 7 + d[n - hundreds * 100] + 3 # +3 for the 'and, +7 for 'hundred'
            else:
                cnt += d[hundreds] + 7 + d[tens] + d[ones] + 3 # +3 for the 'and;
    else:
        cnt += d[n]
    
    return cnt


def count_letters_below_1000():
    ''' Calculate the number of letters for all numbers between 1 and 1000 inclusive when written
            in British English.
    
    Returns:
        The number of letters in all numbers between 1 and 1000 inclusive as an integer.
    '''

    count = 0
    for i in range(1, 1001):
        count += count_letters(i)
    return count


if __name__ == "__main__":
    strt = time()
    count = count_letters_below_1000()
    end = time()
    print(f"Number of total letters in all numbers from 1 to 1000 is: {count}")
    print('------------------------------------------------\n------------------------------------------------')
    print(f"Time taken: {end - strt} s")