#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 10
#
# q: Find the sum of all primes less than 2000000
# a: 142913828922
#

from helpers.prime import sieve_eratosthenes, is_prime

LIMIT = 2000000

''' ---- a slower approach using is_prime() ----
ans = 2
i = 3
while i < LIMIT:
    if is_prime(i): ans += i
    i += 2
'''


primes = sieve_eratosthenes(LIMIT)
ans = 0
for i in range(0, len(primes)):
    if primes[i]: ans += i

print "p10: " + str(ans)

