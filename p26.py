#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 26
#
# q: Find d such that 1/d has the longest recurring cycle
# a: 982
#

def cycle_length(n):
    rem_seen = set()
    cycle_length = 0
    x = 1
    while x%n not in rem_seen:
        cycle_length += 1
        rem_seen.add(x%n)
        x = x%n * 10
    return cycle_length

longest = 0
for i in range(1, 1000):
    pos = cycle_length(i)
    if pos > longest: 
        longest = pos
        ans = i
print "p26: " + str(ans)

