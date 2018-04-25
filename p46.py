#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 45
#
# q:
# a:
#

from helpers.prime import sieve_eratosthenes

sieve = sieve_eratosthenes(10000)
sqs = set()
for i in range(1, 100): sqs.add(2*i**2)
for i in range(9, len(sieve), 2):
    if not sieve[i]:
        found = False
        for j in range(i-2, 0, -2):
            if sieve[j] and i - j in sqs: 
                found = True 
                break
        if not found:
            ans = i
            break
print "p46: " + str(ans)

