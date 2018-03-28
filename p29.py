#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 29
#
# q: Find the number of distinct numbers in the sequence formed by a^b for a,b in [2,100]  
# a: 9183

nums = set()
for a in range(2, 101):
    for b in range(2, 101): nums.add(a**b)
print "p29: " + str(len(nums))

