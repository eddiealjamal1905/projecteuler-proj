# To time speed of the program.
from time import time
import numpy as np
def pythogorean_trip_sum(sum_of_triplet):
    '''Find the pythogorean triplets that sum to a given number and give the product of each of these triplets.
    
    Args:
        sum_of_triplet: The sum of the wanted pythogorean triplet.
        
    Returns:
        pythog_list: A list of tuples each containing a Pythogorean triplet that adds to the given sum.
        prod_list: A list of products of each Pythogorean triplet that add to the sum given.
    '''

    pythog_list = []
    prod_list = []
    for i in range(1,sum_of_triplet + 1):
        for j in range(i,sum_of_triplet):
            c = np.sqrt(i**2 + j**2)
            if (i + j + c == sum_of_triplet):
                pythog_list.append((int(i),int(j), int(c)))
                prod_list.append(int(i*j*c))
    return pythog_list, prod_list

if __name__ == "__main__":
    N = int(input('Enter desired sum for the Pythagorean triplet: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt= time()
    pythog_list, prod_list = pythogorean_trip_sum(N)
    # Looking at pythog_list and prod_list, we have the same triplet and products, (just switched a and b)
    if len(pythog_list) > 0:
        print(f"The Pythogorean triplet(s) that sum to {N} are: {pythog_list}")
        print(f"The product(s) of these triplets is given by: {prod_list}")
    else:
        print("There is no Pythogorean triplets that add to the sum you entered.")
    print('------------------------------------------------\n------------------------------------------------')
    end = time()
    print(f'Time taken: {end-strt} s')