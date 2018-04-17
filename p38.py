#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 
#
# q: Find the largest pandigital number...
# a: 932718654
#

from helpers.pandigital import is_pandigital

def concat_prod(n):
    prod = ''
    i = 1
    while len(prod) < 9:
        prod += str(n*i)
        i += 1
    if len(prod) == 9: return prod
    else: return ''
ans = 0
for i in range(1, 1000000):
    pos = concat_prod(i)
    if len(pos) == 9 and is_pandigital(pos) and int(pos) > ans:
        ans = int(pos)
print "p38: " + str(ans)

