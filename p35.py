#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 35
#
# q: Find the number of circular primes under 1000000
# a: 55
#

from helpers.prime import is_prime

def is_circular_prime(n, num_digs):
    cp = num_digs
    while cp > 0:
        n = ((n%10)*10**(num_digs-1)) + n/10
        if not is_prime(n): return False
        cp -=1
    return True

LIMIT = 1000000
num_digs = 0 
ans = 0
i = 1
while i < LIMIT:
    num_digs += 1
    while i < 10**num_digs:
        if is_circular_prime(i, num_digs): ans += 1
        i += 1
print "p35: " + str(ans)

