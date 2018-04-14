#!/usr/bin/env python



def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n - 1)

def factorial_list(limit):
    l = [1, 1]
    for i in range(1, limit): l.append(l[i] * (i+1))
    return l

def binomial_coefficient(n, k): return factorial(n) / (factorial(n - k) * factorial(k))
