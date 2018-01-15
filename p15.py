#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 15
#
# q: Find the number of lattice paths on a 20x20 grid
# a: 137846528820
#

from helpers.binocoef import binomial_coefficient

print "p15: " + str(binomial_coefficient(40,20))

