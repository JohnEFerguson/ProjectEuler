#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 40 
#
# q: Find the 1st, 10th, ... , 1000000th digit of Champernowne's constant
# a: 210
#

ans = 1
dig = 10
now = 0
for i in range(1, 1000000):
    now += len(str(i))
    if now > dig:
        ans *= int(str(i)[len(str(i)) - (now - dig) - 1])
        dig *= 10
print "p40: " + str(ans)

