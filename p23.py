#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 23
#
# q: Find the sum of all numbers which cannot be written as the sum of two abundant numbers
# a: 4179871
#

from helpers.divisors import sum_divisors

def is_abundant(n): return sum_divisors(n) > n

LIMIT = 28123

ab_nums = set()
for i in range(12, LIMIT):
    if is_abundant(i): ab_nums.add(i)

''' slow
def is_abundant_sum(n):
    for i in range(0, len(ab_nums)):
        if ab_nums[i] >= n: return False
        for j in range(0, len(ab_nums)):
            if ab_nums[i] + ab_nums[j] > n: break
            elif ab_nums[i] + ab_nums[j] == n: return True 
    return False
'''
def is_abundant_sum(n):
    for ab in ab_nums:
        if ab >= n: return False
        if n - ab in ab_nums: return True
    return False

ans = 0
for i in range(0,LIMIT):
    if not is_abundant_sum(i): ans += i
print "p23: " + str(ans)

