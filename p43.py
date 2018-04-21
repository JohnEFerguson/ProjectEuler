#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 
#
# q: 
# a: 
#

from helpers.pandigital import get_pandigital_nums

primes = [0,2,3,5,7,11,13,17]
def substr_divisible(num):
    if len(num) != 10: return False
    for i in range(1,len(num) - 2):
        if int(num[i:i+3])%primes[i] != 0: return False
    return True
#print substr_divisible('1406357289')
#exit()        
nums = get_pandigital_nums('0123456789') 

ans = 0
for num in nums:
    if substr_divisible(num): ans += int(num)
print "p43: " + str(ans)

