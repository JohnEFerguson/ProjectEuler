#!/usr/bin/env python

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

def sieve_eratosthenes(limit):
  primes = [True] * limit
  for i in range(2, limit):
    if not primes[i]: continue
    for j in range(i+i, limit, i): primes[j] = False
  primes[0] = False 
  primes[1] = False
  return primes


