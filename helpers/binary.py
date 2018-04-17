#!/usr/bin/env python

def binary_string(n):
    res = ''
    while n > 0:
        res = str(n&1) + res
        n >>= 1
    return res


    
