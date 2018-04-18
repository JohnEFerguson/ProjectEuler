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

nums = []
def get_pandigital_nums(so_far, left):
    if left == '': nums.append(int(so_far))
    else:
        for i in range(0, len(left)): get_pandigital_nums(so_far + left[i], left[:i] + left[i+1:])

get_pandigital_nums('', '1234567') # there are no primes that are 9,8-dig pandigital

ans = 0
for num in nums:
    if num > ans and is_prime(num): ans = num
print "p41: " + str(ans)

