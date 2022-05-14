 # To time speed of the program.
from time import time

### We write two functions, one which gives the Collatz chain, called collatz_chain, for academic reasons
### and from this we can find the length of the Collatz chain easily, but this function is a bit slower since
### we keep the values in the chain in memory. The other function, collatz_length gives us the length of the
### chain only which saves on memory and time. We combine them to make a fast function that gives the length of
### the longest chain under some upper bound, the number that gives this chain and the chain itself for that number.

def collatz_length(n):
    ''' Calculate the length of the Collatz chain of the input.

    Args:
        n: The positive integer for which we want to find the length of the Collatz Chain.
    
    Returns:
        An integer denoting the length of the Collatz chain of the input, n.
    '''

    cltz_cnt = 1
    while n > 1:
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        cltz_cnt += 1
        
    return cltz_cnt


def collatz_chain(n):
    ''' Calculate the entire Collatz chain of the input.

    Args:
        n: The positive integer for which we want to calculate the Collatz chain.

    Returns:
        A list containing the Collatz chain of the input, n, in descending order.
    '''

    cltz_chain = [n]
    while n > 1:
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        cltz_chain.append(int(n))
        
    return cltz_chain

def longest_collatz(upper_bound):
    ''' Finds the number, that is less than the given input upper bound, that has the longest Collatz
            chain along with the length of that Collatz chain and displays the chain itself.

    Args:
        upper_bound: We only consider the Collatz chains of numbers under this upper bound.
    
    Returns:
        A dictionary with the keys: 'number' which contains the value of the number with the longest 
        Collatz chain, 'chain_length' containing the length of that Collatz Chain, and finally 
        'chain' which contains a list of the Collatz chain in descending order.    
    '''

    n = 1
    largest = 0
    while n < upper_bound:
        length = collatz_length(n)
        if length > largest:
            largest = length
            colz_num = n
            colz_chain = collatz_chain(n)
        n += 1
        
    return {'number': colz_num,
            'chain_length': largest,
            'chain': colz_chain}

if __name__ == "__main__":
    N = int(input('Enter desired upperbound for starting number: '))
    print('------------------------------------------------\n------------------------------------------------')
    strt = time()

    d = longest_collatz(N)
    print(f"The starting number below {N} that gives maximum length of Collatz chain is: {d['number']}\n")
    print(f"The length of the Collatz chain of {d['number']} is: {d['chain_length']}\n")
    print(f"The Collatz chain of {d['number']} is:\n {d['chain']}\n")

    end = time()
    print('------------------------------------------------\n------------------------------------------------')
    print(f'Time taken: {end - strt} s')