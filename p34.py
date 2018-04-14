#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 34
#
# q: Find the sum of numbers which are equal to the sum of their factorial(digits)
# a: 40730
#

from helpers.binocoef import factorial_list

facts = factorial_list(10)
def is_sum_digit_factorials(n):
    n_str = str(n)
    pos = 0
    for c in n_str:
        pos += facts[int(c)]
    return pos == n

ans = 0
for i in range(10,1000000):
    if is_sum_digit_factorials(i): 
        ans += i
print "p34: " + str(ans)

