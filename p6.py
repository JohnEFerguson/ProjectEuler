#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 6
#
# q: find the difference betweent the sum squares and square of the sum for x in {1..100} 
# a: 25164150
#

LIMIT = 101
sum_sq = 0
sq_sum = 0

for i in range(1, LIMIT):
    sum_sq += i**2
    sq_sum += i
sq_sum *= sq_sum

print "p6: " + str(abs(sq_sum - sum_sq))
