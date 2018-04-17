#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 37
#
# q: Find the sum of all 11 truncatable primes 
# a: 748317
#

from helpers.prime import is_prime

def is_truncatable_prime(n):
    cp = n
    p = 10
    while cp >= 1:
        if (not is_prime(n%p)) or (not is_prime(cp)): return False
        cp /= 10
        p *= 10
    return True

ans = 0
for i in range(10, 1000000):
    if is_truncatable_prime(i):
        ans += i
print "p37: " + str(ans)

