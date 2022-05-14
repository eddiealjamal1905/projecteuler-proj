 # To time speed of the program.
from time import time
import numpy as np

def row_products(int_grid_arr, num_adj, largest = 0):
    '''Calculates the largest product of a given number of integers in row inside a grid of integers.
            Transposing the grid of integers and then using this function gives the largest product
            for columns instead of rows.

    Args:
        int_grid_arr: the grid of integers as a string.
        num_adj: the number of adjacent grid numbers in a row
             that we want to consider for the product.
        largest: initial integer to compare largest product to
       
    Returns:
        Largest which is the largest product along the rows of (num_adj) integers in the 
            grid and index position of these numbers.
    '''

    indices_arr = None
    for i in range(int_grid_arr.shape[0]):
        for j in range(int_grid_arr.shape[1] - num_adj + 1):
            prod = 1
            for k in range(num_adj):
                prod *= int_grid_arr[i,j + k]
                if prod > largest:
                    largest = prod
                    indices_arr = [(i,j + k) for k in range(num_adj)]
    return largest, indices_arr

def diag_products(int_grid_arr, num_adj, largest = 0):
    '''Calculates the largest product of a given number of integers in negative-sloped 
        diagonal inside a grid of integers. Once we mirror flip the grid and use this function
        on the resultant integer grid, we will get the largest product of a positive-sloped diagonal.

    Args:
        int_grid_arr - the grid of integers as a string.
        num_adj - the number of adjacent grid numbers in a diagonal
            that we want to consider for the product.
        largest - initial integer to compare largest product to.
       
    Returns:
        Largest product along the negative-sloped diagonal of (num_adj) integers in the grid
            and index position of these numbers.
    '''

    indices_arr = None
    for i in range(int_grid_arr.shape[0] - num_adj + 1):
        for j in range(int_grid_arr.shape[1] - num_adj + 1):
            prod = 1
            for k in range(num_adj):
                prod *= int_grid_arr[i + k,j + k]
                if prod > largest:
                    largest = prod
                    indices_arr = [(i + k,j + k) for k in range(num_adj)]
    return largest, indices_arr

def index_flip(x, size):
    '''Given the matrix indices of some arbitrary entry in an integer grid/matrix, we 
            give the corresponding indices that entry will have when the grid is mirror flipped.

    Args:
        x: 2-element tuple of indices of an entry in the grid.
        size - size of the grid
       
       Returns: the corresponding grid indices in the mirrored grid (after applying np.flip()).
    '''

    arr = list(reversed(range(-size, size + 1,2)))
    return (x[0], x[1] + arr[x[1]])


def grid_adj_product(grid_str, num_adj = 4):
    '''Calculate the largest product of given number of integers (defaulted to 4) in a row, column
            positive- & negative-sloped diagonal in the grid, then calculate the maximum product overall.
    
    Args:
        grid_str - A string literal a grid of integers.
       num_adj - the number of adjacent grid numbers that we want to consider for the product.
       
       Returns: 
            d: a dictionary of the products where the key's are the "column", "row", "negative diagonal", 
            "positive diagonal" and the values of the keys are tuples where the first entry is the largest product
            in that line and the second entry is a list of index positions of the numbers that give this product.
            the max of these products and the indices of numbers in the grid yielding this max product.
    '''
    
    int_grid_arr = np.array([list(map(int, i.split())) for i in grid_str.split('\n')])
    largest_in = 0
    # Row products
    largest_row, indices_arr_row = row_products(int_grid_arr, num_adj, largest_in)
    
    # Column products: We use the same function that produces the row product but on the transposed grid
    largest_col, indices_arr_col = row_products(int_grid_arr.T, num_adj, largest_in)
    # Since we transposed the grid, the indices given in indices_arr_col are indices of the transposed grid
    # so we flip them
    indices_arr_col = [indices_arr_col[i][::-1] for i in range(len(indices_arr_col))]
    
    # diagonal (negative slope) products
    largest_diag1, indices_arr_diag1 = diag_products(int_grid_arr, num_adj, largest_in)
    
    # diagonal (positive slope products): We use the same function that produces the negatively sloped diagonal
    # products above on the mirrored (np.flip) grid along the vertical axis.
    largest_diag2, indices_arr_diag2 = diag_products(np.flip(int_grid_arr, axis = 1), num_adj, largest_in)
    # Since we mirrored the grid, the indices given in indices_arr_diag2 are indices of the mirrored grid
    # so we convert them to the indices of the original grid
    indices_arr_diag2 = list(map(lambda x: index_flip(x, int_grid_arr.shape[0]-1), indices_arr_diag2))
    
    result = {largest_col: indices_arr_col, largest_row: indices_arr_row, largest_diag1: indices_arr_diag1, 
             largest_diag2: indices_arr_diag2}
    mx = max(result)
    
    d = {"column": (largest_col, indices_arr_col),
         "row": (largest_row, indices_arr_row),
         "negative diagonal": (largest_diag1, indices_arr_diag1),
         "positive diagonal": (largest_diag2, indices_arr_diag2)}

    return d, (mx, result[mx])


if __name__ == "__main__":
    numbers_str = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

    strt = time()
    int_grid_arr = np.array([list(map(int, i.split())) for i in numbers_str.split('\n')])
    prod_dict, (largest_prod, largest_prod_ind) = grid_adj_product(numbers_str, 4)
    num_adj = len(prod_dict['row'][1])
    print(f'*The greatest product of {num_adj} adjacent numbers in the above 20x20 grid is: {largest_prod}.\n')
    print(f'''*The numbers that give the largest product {largest_prod} are at
    grid (starting at index 0) index locations: {largest_prod_ind}.\n''')

    largest_ind_new = [],[]
    # We can write a list comprehension for this but it will involve two loops.
    for x in largest_prod_ind:
        largest_ind_new[0].append(x[0])
        largest_ind_new[1].append(x[1])
    print(f'''*The numbers that give the largest product are {int_grid_arr[largest_ind_new]}.''')
    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time Taken: {end - strt} s')
