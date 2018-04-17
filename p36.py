#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 36
#
# q: Find the sum of all numbers less than 1000000 which are a palindrome in decimal and binary representations
# a: 
#

from helpers.binary import binary_string
from helpers.palindrome import is_palindrome_str

LIMIT = 1000000
ans = 0
for i in range(0, LIMIT):
    if is_palindrome_str(str(i)) and is_palindrome_str(binary_string(i)):
        ans += i
print "p36: " + str(ans)

