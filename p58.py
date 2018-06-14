#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 58
#
# q: 
# a: 
#
# this one needs a little work, right idea but there is a problem with the implementation

from __future__ import division
from helpers.prime import is_prime

side = 3
diags = 2
prime_diags = 1
num = 5
i = 2
inc = 2
while prime_diags/diags >= .10:
    diags += 1
    if is_prime(num): prime_diags += 1
    num += inc
    i += 1
    if i == 4: 
        i = 0
        inc += 2
        side += 2
print 'p58: ' + str(side-2)

