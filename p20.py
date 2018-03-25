#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 20
#
# q: Find the sum of the digits in the number 100!
# a: 648
#

from helpers.bignumber import BigNumber

num = BigNumber('100')
num.factorial(100)
print "p20: " + str(num.sum_digits())

