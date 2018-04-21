#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 
#
# q: Find the largest n-digit pandigital prime
# a: 7652413
#

from helpers.prime import is_prime
from helpers.pandigital import get_pandigital_nums

nums = get_pandigital_nums('1234567') # there are no primes that are 9,8-dig pandigital

ans = 0
for num in nums:
    if int(num) > ans and is_prime(int(num)): ans = int(num)
print "p41: " + str(ans)

