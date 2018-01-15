#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 14
#
# q: Find n < 1000000 the collatz sequence starting at n is maximized
# a: 837799
#

LIMIT = 1000000

collatz = [0]*LIMIT

def collatz_length(n, orig, so_far):
    if n < LIMIT and collatz[n] != 0:
        collatz[orig] = so_far + collatz[n] - 1
        return so_far + collatz[n] - 1
    elif n == 1:
        collatz[orig] = so_far
        return so_far
    elif n%2 == 0: return collatz_length(n/2, orig, so_far + 1)
    else: return collatz_length(n*3 + 1, orig, so_far + 1)

max_length = 0
i = 1
while i < LIMIT:
    pos = collatz_length(i, i, 1)
    if pos > max_length: 
        max_length = pos
        ans = i
    i += 1

print "p14: " + str(ans)

