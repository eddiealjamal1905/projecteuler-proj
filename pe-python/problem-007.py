# To time speed of the program.
from time import time

# From Wikipedia about fast prime algorithms.
# The simplest primality test is trial division: given an input number, n, check whether it is evenly divisible 
# by any prime number between 2 and √n (i.e. that the division leaves no remainder). If so, then n is composite. 
# Otherwise, it is prime.
# For example, consider the number 100, which is evenly divisible by these numbers:
# 2, 4, 5, 10, 20, 25, 50
# Note that the largest factor, 50, is half of 100. This holds true for all n: all divisors are less than or equal 
# to n/2.
# Actually, when we test all possible divisors up to n/2, we will discover some factors twice. 
# To observe this, rewrite the list of divisors as a list of products, each equal to 100:
# 2 × 50, 4 × 25, 5 × 20, 10 × 10, 20 × 5, 25 × 4, 50 × 2.
# Notice that products past 10 × 10 merely repeat numbers which appeared in earlier products. 
# For example, 5 × 20 and 20 × 5 consist of the same numbers. This holds true for all n: all unique divisors of n are numbers less than or equal to √n, so we need not search past that.[1] (In this example, √n = √100 = 10.)
# All even numbers greater than 2 can also be eliminated since, if an even number can divide n, so can 2.
# Let's use trial division to test the primality of 17. We need only test for divisors up to √n, 
# i.e. integers less than or equal to √17 ≈ 4.12, namely 2, 3, and 4. We can skip 4 because it is an 
# even number: if 4 could evenly divide 17, 2 would too, and 2 is already in the list. 
# That leaves 2 and 3. We divide 17 with each of these numbers, and we find that neither divides 17 
# evenly—both divisions leave a remainder. So, 17 is prime.
# We can improve this method further. Observe that all primes greater than 3 are of the form 6k ± 1, 
# where k is any integer greater than 0. This is because all integers can be expressed as (6k + i), 
# where i = −1, 0, 1, 2, 3, or 4. Note that 2 divides (6k + 0), (6k + 2), and (6k + 4) and 3 divides (6k + 3).
# So, a more efficient method is to test whether n is divisible by 2 or 3, then to check through all numbers of the 
# form 6k ± 1 ≤ √n. This is 3 times faster than testing all numbers up to √n.

def isPrime(n):
    '''Check if a mumber is a prime number usig the 6k +/- 1 optimization described above.
    Args:
        n: The number that we check if it is prime or not.

    Returns:
        Boolean True if the input is [rime, otherwise returns False.
    '''

    # Check corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    
    # We want to check if 6k +/- 1 is divisible by the integers less than or equal sqrt{n}
    # but we now that some numbers in the form of 6k +/- 1 for some k are divisible by 2 or 3 or both
    # like 6k + 4 and/or 6k + 3. So we have to check divisibility of n by 2 or 3 first to make it more efficient
    # and not check if n is divisible by numbers like 6k + 0, 6k + 2, ... or 6k+3, 6k + 9, ...
    # and if n is divisible by these numbers it has to be divisible by 2 or 3. 
    
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    # Now, we carry on with the 6k +/- 1 optimization (which includes all primes as mentioned above)
    # starting at k = 1 (which gives 5 initially). 
    # So, we check if n is divisible by 6k - 1 or 6k + 1 = (6k - 1) + 2 for each number less than or equal to 
    # sqrt n. The addition i = i + 6 is because of the 6k where k is a positive integer now, so that we are
    # stepping by steps of 6.
    
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


def mth_prime(m):
    '''This give the (m)th prime number. For example, 2 is the 1st prime and 3 is the 2nd prime'''
    if m == 1:
        return 2
    else:
        n = 1
        prime_cnt = 1
        while (prime_cnt < m):
            n += 2   # start at 3 and icrement by 2 to check odd numbers
            if isPrime(n):
                prime_cnt += 1 
    return n

def mth_prime(m):
    '''This give the (m)th prime number. For example, 2 is the 1st prime and 3 is the 2nd prime.
    
    Args:
        m: The cardinal or index of required prime number.
        
    Returns:
        If m is the input, then this returns the mth prime number.
    '''

    if m == 1:
        return 2
    else:
        n = 1
        prime_cnt = 1
        while (prime_cnt < m):
            n += 2   # start at 3 and icrement by 2 to check odd numbers
            if isPrime(n):
                prime_cnt += 1 
    return n

if __name__ == "__main__":
    prime_ind = int(input('Please enter the cardinal number for the desired prime (For example, enter 2 for the second prime number): '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    ans = mth_prime(prime_ind)
    print(f"The {prime_ind}th prime is: {ans}")
    end = time()
    print(f'Time taken: {end-strt} s')