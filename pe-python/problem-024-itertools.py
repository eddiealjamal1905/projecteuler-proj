 # To time speed of the program.
from time import time
from itertools import permutations

def lexicographic_perm(length, m):
    ''' Calculate the permutation of a list of integers from 0 to (length) and put them in lexicographic
            order and extract the (m)th permuation of that order.
    
    Args:
        length: length of the array of consecutive integers starting from 0 to permute.
        m: the index of the particular permutation we want to see within the lexicographic list of all 
            permutations. That is we display the mth lexicographic permutation
           
    Returns:
        a tuple; the first element of which is list of all possible permutations of the array of consecutive
        integers starting at 0 in lexicographic order as lists; the second element of that tuple is the mth 
        lexicographic permutation given as an integer.
    '''

    integer_list = range(length)
    perms = permutations(integer_list) # This is already in lexicographic order.
    m_perm = int(''.join(map(str, list(perms)[m-1])))

    return perms, m_perm


if __name__ == "__main__":
    length = int(input('Please enter the length of the original array we want to permute: '))
    m = int(input('Please enter the index of the lexicographic permutation you are interested in seeing: '))
    print('------------------------------------------------\n------------------------------------------------')

    strt = time()
    perms, m_perm = lexicographic_perm(length, m)
    end = time()

    print(f"The {m}th lexicographic permutation of {list(range(length))} is: {m_perm}")
    print('------------------------------------------------\n------------------------------------------------')
    print(f"Time taken: {end - strt}s")