#!/usr/bin/env python

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n - 1)

def binomial_coefficient(n, k): return factorial(n) / (factorial(n - k) * factorial(k))
