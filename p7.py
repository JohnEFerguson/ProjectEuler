#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 7
#
# q: Find the 10001st prime
# a: 104743
#

from helpers.is_prime import is_prime 

NUM = 10001

num_prime = 0
ans = 0
while num_prime != NUM:
    ans += 1    
    if is_prime(ans): num_prime += 1
    
print "p7: " + str(ans)

