#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 48
#
# q: Find the last 10 digs of 1^1 + ... + 1000^1000
# a: 9110846700
#

ans = 0
for i in range(1, 1001): ans += i**i
print "p48: " + str(ans)[-10:]

