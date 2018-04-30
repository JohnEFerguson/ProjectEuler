#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 47
#
# q: Find the first of 4 consecutive integers each with 4 distinct prime factors
# a: 134043
#

from helpers.prime import sieve_eratosthenes
from math import sqrt

sieve = sieve_eratosthenes(100000)
l = 1000000

ans = 0
cons = 0
for i in range(644, l):
    p_facs = set()
    for j in range(2, int(sqrt(i) + 1)):
        if i%j == 0:
            if sieve[j]: p_facs.add(j)
            if sieve[i/j]: p_facs.add(i/j)
    if len(p_facs) == 4: 
        cons += 1
    else: cons = 0
    if cons == 4:
        ans = i - 3
        break
print "p47: " + str(ans)

