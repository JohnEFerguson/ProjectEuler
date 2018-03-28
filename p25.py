#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 25
#
# q: 
# a: 
#

a = 1
b = 1
ans = 2
while len(str(b)) < 1000:
    temp = a
    a = b
    b += temp
    ans += 1
print "p25: " + str(ans)

