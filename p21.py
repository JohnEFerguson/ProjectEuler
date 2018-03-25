#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 21
#
# q: 
# a: 
#

from helpers.divisors import sum_divisors

def is_amicable(a):
    d_a = sum_divisors(a)
    d_b = sum_divisors(d_a)
    return [d_b == a and a != d_a, d_a]

ans = 0
checked_nums = set()

for i in range(1, 10001):
    if i not in checked_nums: 
        is_am = is_amicable(i)
        if is_am[0]:
            ans += i + is_am[1]
            checked_nums.add(is_am[1])
print "p21: " + str(ans)

