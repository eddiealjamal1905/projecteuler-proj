def sum_multiples(factor1, factor2, upper_bound = 1000):
    '''Find the sum of multiples of either (factor1) or (factor2) (or both) under (upper_bound)'''
    s = 0
    cnt = 0
    for i in range(1, upper_bound):
        if i % factor1 == 0 or i % factor2 == 0:
            s += i
            cnt += 1
    return s, cnt

from time import time
f1, f2 = tuple(map(int,input('Enter the two factors separated by a space:').split()))
upbnd = int(input('Enter the the upperbound for the search of multiples:'))
print('-------------------------------------------\n-------------------------------------------')

strt = time()
s, cnt = sum_multiples(f1, f2, upbnd)
print(f"sum of multiples of {f1} or {f2} below {upbnd} is: {s}")
print(f"Number of multiples of {f1} or {f2} below {upbnd} is: {cnt}")

end = time()
print('-----------------------------------------\n-----------------------------------------')
print(f'Time taken: {end - strt} s')