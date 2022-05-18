 # To time speed of the program.
from time import time

# For this problem, we will make use of Heap's algorithm to generate all possible permutations
# of a list of objects. We could have generated the list of all permutations using itertools 
# library as well.


def swap_list(A,i,j):
    ''' Swaps two entries in a vector.
    
    Args:
        A: indexable array type.
        i,j: index integers of array A. So that A[i] and A[j] will be swapped in A.

    Returns; Nothing, but modifies the array by reference as it is an iterable.
    '''

    A[i], A[j] = A[j], A[i]


def heap_perm_recurs(n, A, B):
    ''' Calculate all possible permutations of a list of integers.
    
    Args:
        n: integer of the size of the array of integers to be permuted, A.
        A: list of integers to be permuted, must be indexable.
        B: the list in which to fill all possible permutations of A as lists.
       
    Returns:
        A modified list B which now contains all possible permutations of A as lists, so B is a list of lists.
    '''

    if n == 1:
        B.append(list(map(str, A)))
    else:
        heap_perm_recurs(n-1, A, B)
        for i in range(n-1):
            if (n % 2 == 0):
                swap_list(A, i, n-1)
            else:
                swap_list(A, 0, n-1)
            heap_perm_recurs(n-1, A, B)
    return B


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

    A = list(range(length))
    B = []
    p = sorted(heap_perm_recurs(length, A, B))
    return p, int(''.join(p[m - 1]))


if __name__ == "__main__":
    length = int(input('Please enter the length of the original array we want to permute: '))
    m = int(input('Please enter the index of the lexicographic permutation you are interested in seeing: '))
    print('------------------------------------------------\n------------------------------------------------')

    strt = time()

    A = list(range(length))
    _, m_perm = lexicographic_perm(length, m)

    end = time()
    print(f"The {m}th lexicographic permutation of {A} is: {m_perm}")
    print('------------------------------------------------\n------------------------------------------------')
    print(f"Time taken: {end - strt}s")