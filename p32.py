#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 32
#
# q: 
# a: 
#

from helpers.divisors import get_divisors

all_digs = set()
for i in range(1, 10): all_digs.add(i)

def is_pandigital(s): 
    if len(s) != 9: return False
    digs = set()
    for dig in s: digs.add(int(dig))
    return digs == all_digs
    
def is_factor_pandigital(n):
    divisors = get_divisors(n)
    for div in divisors:
        digs = str(n)
        digs += str(div) + str(n/div)
        if is_pandigital(digs): return True
    return False

ans = 0
for i in range(0, 10000):
    if is_factor_pandigital(i): ans += i
print "p32: " + str(ans)

