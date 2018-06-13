#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 53
#
# q: 
# a: 
#

from helpers.binocoef import binomial_coefficient

ans = 0
for n in range(1, 101):
    for r in range(1, n):
        if binomial_coefficient(n, r) > 1000000: ans += 1
print 'p53: ' + str(ans)

