#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 39 
#
# q: 
# a: 
#

sols = {}
sq_difs = {}
for c in range(1,1000):
    for b in range(1,c):
        if c*c - b*b in sq_difs: sq_difs[c*c - b*b].append([b,c])
        else: sq_difs[c*c - b*b] = [[b,c]]


for a in range(0, 1000):
    if a*a in sq_difs:
        for b_c in sq_difs[a*a]: 
            if a + b_c[0] + b_c[1] in sols: sols[a + b_c[0] + b_c[1]] += 1
            else: sols[min(a + b_c[0] + b_c[1], 1001)] = 1
print "p39: " + str(max(sols, key=sols.get))

