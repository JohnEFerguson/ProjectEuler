#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 45
#
# q: Find the biggest T_n after T_285 s.t. T_n is also pentagonal and hexagonal
# a: 1533776805
#

LIM = 100000
pents = set()
tris = set()
hexs = set()
for i in range(285, LIM): 
    tris.add(i*(i + 1)/2)
    pents.add(i*(3*i - 1)/2)
    hexs.add(i*(2*i - 1))

ans = 0
for num in tris:
    if num in pents and num in hexs: 
        ans = num
        break
print "p45: " + str(ans)

