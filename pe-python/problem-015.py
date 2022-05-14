 # To time speed of the program.
from time import time
from math import factorial

def lattice_paths(n):
    ''' Calculates the number of paths to get from the upper left corner to the lower right corner
            of an n x n square grid—by moving either down and to the right, where n is the input.

    Args:
        n: size of the square grid.
    
    Return: 
        The number of possible paths from the upper left corner to lower right corner.
    '''
    # We have to traverse 2n sizes, n down and n to the right, we just have to choose their order.
    return int(factorial(2*n)/factorial(n)**2)

if __name__ == "__main__":
    size = int(input('Enter the size of the square grid: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()
    num_paths = lattice_paths(size)
    print(f"Number of total paths for the grid of size {size} x {size} is: {num_paths}")
    print('------------------------------------------------\n------------------------------------------------')
    end = time()
    print(f"Time taken: {end - strt} s")