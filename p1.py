#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 1
#
# q: Find the sum of all multiples of 3 or 5 below 1000
# a: 233168
#

ans = 0
for i in range(3, 1000):
    if i%3 == 0 or i%5 == 0: ans += i
print "p1: " + str(ans)

