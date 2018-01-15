#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 13
#
# q: Find the first 10 digits of the sum of 100 50-digit numbers 
# a: 5537376230
#

from helpers.bignumber import BigNumber

ans = 0

n = BigNumber('2')
n.pow(1000)

for i in str(n):
    ans += (int(i))
print "p16: " + str(ans)
