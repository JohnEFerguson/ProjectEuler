#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 51
#
# q: 
# a: 
#

from helpers.prime import sieve_eratosthenes

LIMIT = 10000000

sieve = sieve_eratosthenes(LIMIT) # get primes

def get_permutation_helper(sofar, left, l):
    if left == 0: l.append(sofar)
    else:
        get_permutation_helper(sofar + '0', left - 1, l)
        get_permutation_helper(sofar + '1', left - 1, l)

def get_permutations(lim):
    l = []
    for i in range(0, lim): 
        l.append([])
        get_permutation_helper("", i, l[i])
    return l

def prime_family(n, perm):
    n_list = list(str(n))
    length = len(n_list)
    ans = []
    for i in range(0, 10):
        for j in range(0, len(perm)):
            if perm[j] == '1': n_list[j] = str(i)
        if len(str(int("".join(n_list)))) == length and sieve[int("".join(n_list))]: ans.append(int("".join(n_list)))
    return ans

perms = get_permutations(8) # get permutations
done = False
for i in range(0, LIMIT/10):
    if not sieve[i]: continue 
    for j in range(0, len(perms[len(str(i))])):
        pos_fam = prime_family(i, perms[len(str(i))][j])
        if len(pos_fam) == 8: 
            ans = pos_fam[0]
            done = True
            break
    if done: break
        
print 'p51: ' + str(ans)

