#!/usr/bin/env python

def is_palindrome(n):
    mag = 1
    cn = n
    while cn >= 10:
        mag += 1
        cn /= 10
    for i in range(1, mag+1):
        if get_dig(n, i) != get_dig(n, mag + 1 - i): 
            return False
    return True

def get_dig(n, i):
    return (n/(10**(i-1)))%10


