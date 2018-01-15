#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 12
#
# q: find the smallest triangular number with over 500 divisors
# a: 76576500 
#

from math import sqrt
from helpers.divisors import count_divisors

def is_triangle(n): 
    a = int(sqrt(2*n))
    return 0.5*a*(a+1) == n

# n must be a triangle number
def last_term(n): return int(sqrt(2*n))

# the smallest number with 500 divisors 
# N = p^a => N has a+1 divisors
pos = 2**4 * 3**4 * 5**4 * 7 * 11

# look for next highest triangle number
while not is_triangle(pos): pos += 1

next = last_term(pos) + 1

while not count_divisors(pos) >= 500: 
    pos += next
    next += 1

print "p12: " + str(pos)

