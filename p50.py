#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 50
#
# q: 
# a: 
#

from helpers.prime import is_prime
primes = []
pos = 0
for i in range(2, 100000):
    if pos > 1000000: break
    if is_prime(i):
        pos += i
        primes.append(i)
ans = 0
max_r = 0
def check_prime_sum(b, e, pos):
    global max_r
    global ans
    if pos < 1000000 and is_prime(pos):
        if e-b > max_r: 
            max_r = e-b
            ans = pos
    elif e-b > max_r: 
        check_prime_sum(b+1, e, pos - primes[b])
        check_prime_sum(b, e-1, pos - primes[e])
check_prime_sum(0, len(primes)-1, pos)
print 'p50: ' + str(ans)
