#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 28
#
# q: Find the sum of all the numbers on the corners of a spiral
# a: 669171001

sum = 1
num = 1
inc = 2
dim = 1
while dim <= 500:
    for i in range(0, 4):
        num += inc
        sum += num
    dim += 1
    inc += 2
print "p28: " + str(sum)

