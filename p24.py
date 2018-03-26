#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 24
#
# q: 
# a: 
#

from helpers.sorting import merge_sort

permutations = []

def add_permutations(sofar, left):
    if len(sofar) == 10:
        permutations.append(sofar)
    else: 
        if len(left) == 1: add_permutations(sofar + left, '')
        else:
            for i in range(0, len(left)):
                add_permutations(sofar + left[i], left[0:i] + left[i+1:])

add_permutations('', '0123456789')

print "p24: " + str(permutations[999999])

