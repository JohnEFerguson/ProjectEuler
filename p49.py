#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 49
#
# q: 
# a: 
#

from helpers.pandigital import get_pandigital_nums
from helpers.prime import is_prime

def check_prime_permutations(i):
    if is_prime(i):
        nums = get_pandigital_nums(str(i))
        pos = set()
        for n in nums:
            if is_prime(int(n)): 
                pos.add(int(n))
                nums.remove(n)
        if len(pos) >= 3: 
            for a in pos:
                for b in pos:
                    if a < b and a + ((b-a)*2) in pos:
                        return str(a) + str(b) + str(a + (b-a)*2)
        else: return ''
    return ''

for i in range(1000, 10000):
    pos = check_prime_permutations(i)
    if len(pos) > 0 and '1487' not in pos: 
        ans = pos
        break
print 'p49: ' + ans                
