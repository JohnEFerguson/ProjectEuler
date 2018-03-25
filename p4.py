#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 4
#
# q: Find the largest product of two 3-digit numbers which is a palindrome
# a: 906609 
#

from helpers.palindrome import is_palindrome 

ans = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        pos = i * j
        if pos > ans and is_palindrome(pos):
            ans = pos 

print "p4: " + str(ans)

