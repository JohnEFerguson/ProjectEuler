#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 9
#
# q: Find a*b*c such that a > b > c, a + b + c = 1000 and a^2 + b^2 = c^2 
# a: 31875000
#

def find_triplet():
    for a in range(1, 999):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return  a * b * c
                
print 'p9: ' + str(find_triplet())

