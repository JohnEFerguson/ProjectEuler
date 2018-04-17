#!/usr/bin/env python

def is_palindrome_int(n):
    mag = 1
    cn = n
    while cn >= 10:
        mag += 1
        cn /= 10
    for i in range(1, mag+1):
        if get_dig(n, i) != get_dig(n, mag + 1 - i): 
            return False
    return True

def is_palindrome_str(s):
    if len(s) < 2: return True
    else: return s[0] == s[-1] and is_palindrome_str(s[1:-1])

def get_dig(n, i):
    return (n/(10**(i-1)))%10


