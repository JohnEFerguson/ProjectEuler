#!/usr/bin/env python

from math import sqrt

def count_divisors(n):
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0: 
            count += 1
            if i*i != n: count += 1 
    return count

