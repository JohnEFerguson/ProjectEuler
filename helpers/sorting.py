#!/usr/bin/env python

def merge_sort(l):
    if len(l) <= 1: return l
    a = merge_sort(l[:len(l)/2])
    b = merge_sort(l[len(l)/2:])
    return merge(a, b)

def merge(a, b):
    m = []
    while len(a) != 0 or len(b) != 0:
        if len(b) == 0 or (len(a) != 0 and a[0] <= b[0]):
            m.append(a[0])
            a = a[1:]
        elif len(a) == 0 or (len(b) != 0 and b[0] <= a[0]):
            m.append(b[0])
            b = b[1:]
    return m



