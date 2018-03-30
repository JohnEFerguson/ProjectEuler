#!/usr/bin/env python

from math import sqrt

def count_divisors(n):
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0: 
            count += 1
            if i*i != n: count += 1 
    return count

def sum_divisors(n):
    sum = 0
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            sum += i
            if n/i != i: sum += n/i
    return sum + 1

def get_divisors(n):
    divs = set()
    for i in range(1, int(sqrt(n)+1)):
        if n%i == 0: 
            divs.add(i)
            divs.add(n/i)
    return divs

''' test code
for i in range(1, 5000):
    if len(get_divisors(i)) != count_divisors(i): print i 
'''
            
    
