#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 44
#
# q: 
# a: 
#
''' This implementation gets the right answer but it's slow
pent_nums = set()
for i in range(1, 10000): pent_nums.add(i*(3*i - 1)/2)

ans = 0
for p_j in pent_nums:
    for p_k in pent_nums:
        if p_j + p_k in pent_nums and abs(p_j - p_k) in pent_nums:
            print "here"
            if ans == 0 or abs(p_j - p_k) < ans:
                ans = abs(p_j - p_k)
'''
from math import sqrt
def is_pentagonal(x): return (sqrt(24*x + 1) + 1)%6 == 0
def pent_num(n): return n*(3*n - 1)/2    

for i in range(1, 1000): 
    if not is_pentagonal(pent_num(i)): 
        print "not working"
        break
ans = 0
found = False
j = 2
while not found:
    p_j = pent_num(j)
    for k in range(j - 1, 0, -1):
        p_k = pent_num(k)
        if is_pentagonal(p_j + p_k) and is_pentagonal(abs(p_j - p_k)):
            ans = abs(p_j - p_k)
            found = True
            break
    j += 1
print "p44: " + str(ans)

