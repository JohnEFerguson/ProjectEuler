#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 2
#
# q: Find the sum of all even fibonacci numbers less than 4000000
# a: 4613732
#

ans = 0
LIMIT = 4000000
t1 = 1
t2 = 2

while t2 < LIMIT:
    if t2%2 == 0: ans += t2
    temp = t2
    t2 = t1 + t2
    t1 = temp

print "p2: " + str(ans)
