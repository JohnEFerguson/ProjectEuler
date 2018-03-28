#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 30
#
# q: Find the sum of all n such that n can be written as a sum of its digits raised to the 5th power 
# a: 443839
#

def sum_digit_powers(n, p):
    sum = 0
    cp = n
    while cp >= 1: 
        sum += (cp%10)**p
        cp /= 10
    return sum == n

power = 5
LIMIT = 1000000 # reduce memory by using a while loop
ans = 0
for i in range(2, LIMIT):
    if sum_digit_powers(i, power): ans += i
print "p30: " + str(ans)

