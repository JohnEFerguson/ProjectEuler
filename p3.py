#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 3
#
# q: Find the largest prime factor of 600851475143
# a: 6857
#

from helpers.prime import is_prime

NUM = 600851475143
ans = 0
n = NUM
i = 2
while i**2 < NUM:
  if n%i == 0:
    n /= i 
    ans = i 
  else: i += 1
if n > ans: ans = n

print "p3: " + str(ans)

