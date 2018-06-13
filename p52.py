#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 52
#
# q: 
# a: 
#

from helpers.sorting import merge_sort

def is_permuted_multiple(n):
    sorted_digs = merge_sort(list(str(n)))
    for i in range(2, 7):
        if sorted_digs != merge_sort(list(str(n*i))):
            return False
    return True

ans = 0
for i in range(1, 1000000):
    if is_permuted_multiple(i):
        ans = i
        break
print 'p52: ' + str(ans)

