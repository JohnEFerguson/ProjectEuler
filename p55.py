#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 55
#
# q: 
# a: 
#
#

from helpers.palindrome import *

def is_lychrel(n):
    it = 0
    while it < 50:
        pal = get_palindrome_int(n)
        if is_palindrome_int(n + pal): return False
        n = pal + n
        it += 1
    return True

ans = 0
for i in range(0, 10000):
    if is_lychrel(i): ans += 1
print 'p55: ' + str(ans)

