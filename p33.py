#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 33
#
# q: Find the product of the 4 digit cancelling fractions (0,1) in lowesr terms 
# a: 100
#

from __future__ import division
from helpers.divisors import gcd

num, den = 1, 1
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if k/i < 1 and int(str(k) + str(j))/int(str(j) + str(i))  == k/i: 
                den *= int(str(j) + str(i)) 
                num *= int(str(k) + str(j))
print "p33: " + str(int(den/gcd(num, den)))

