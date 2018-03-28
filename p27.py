#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 27
#
# q: Find the product ab such that n^2 + an + b produces the longest sequence of primes
# a: -59231
#

from helpers.prime import sieve_eratosthenes

sieve = sieve_eratosthenes(100000) # find a programmatic way of finding a limit for this?

def consecutive_primes(a, b):
    ans = 0
    for n in range(0, 100):
        if sieve[n*n + a*n + b]: ans += 1
        else: return ans
    return ans

ans = 0 
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
       pos = consecutive_primes(a, b) 
       if pos > ans: 
           ans = pos
           product = a*b
print "p27: " + str(product)

