# To time speed of the program.
from time import time
import numpy as np


def adj_num_largest_prod(number, num_adj_digits = 4):
    '''Find the largest product that can be made from a desired number of adjacent 
        digits in a given positive integer.
        
    Args:
        number: The number whose digits will be searched for largest product.
        num_adj_digits: The number of adjacent digits to consider for a product.
        
    Returns:
        lrgest_prod: largest product of a given number of adjacent digits in the given number.
        lrgst_seq: The sequence of adjacent integers that give the largest product in the given number.
    '''

    lrgst_prod = 0
    strnum = str(number)
    l = len(strnum)
    for i in range(l-num_adj_digits + 1):
        prod = 1
        for j in range(num_adj_digits):
            prod *= int(strnum[i+j])
        if prod > lrgst_prod:
            lrgst_prod = prod
            first_num = i
    lrgst_seq = [int(strnum[first_num + x]) for x in range(num_adj_digits)]
    return lrgst_prod, lrgst_seq

if __name__ == "__main__":
    num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    number = int(num)

    adj = int(input('Please enter the desired number of adjacent digits to be considered: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    largest_prod, prod_seq = adj_num_largest_prod(number, num_adj_digits = adj)
    print(f"Largest product of {adj} adjacent digits in the number given is: {largest_prod}")
    print(f"The sequence of {adj} adjacent digits in the number that led to the Largest product is: \n {prod_seq}")
    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end-strt} s')