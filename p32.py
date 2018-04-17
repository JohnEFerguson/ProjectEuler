#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 32
#
# q: 
# a: 
#

from helpers.pandigital import is_factor_pandigital

ans = 0
for i in range(0, 10000):
    if is_factor_pandigital(i): ans += i
print "p32: " + str(ans)

