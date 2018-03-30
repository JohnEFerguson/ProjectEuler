#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 31
#
# q: Find the number of ways you can make 200p with coins 1, 2, 5, 10, 20, 50, 100, and 200 
# a: 73682
#

total = 200
sizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * (total + 1)
ways[0] = 1 # one way to make 1p with 1p
for size in sizes: 
    for i in range(size, total + 1): ways[i] += ways[i - size]
print "p31: " + str(ways[-1])

