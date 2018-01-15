#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 13
#
# q: Find the first 10 digits of the sum of 100 50-digit numbers 
# a: 5537376230
#

from helpers.bignumber import BigNumber

file_name = 'data/p13_nums.txt'

f = open(file_name, 'r')
nums = []
for line in f: nums.append(line[:-1])

ans = BigNumber(nums[0])
for num in nums[1:]: ans.add(BigNumber(num))

print "p13: " + str(ans)[:10]

