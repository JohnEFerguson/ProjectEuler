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

def digit_sum(n):
    ans = 0
    while n >= 1:
        ans += n%10
        n /= 10
    return ans

ans = 0
for a in range(0, 100):
    for b in range(0, 100):
        pos = digit_sum(a**b)
        if pos > ans: ans = pos
print 'p56: ' + str(ans)

