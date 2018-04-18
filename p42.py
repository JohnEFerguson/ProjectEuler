#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 22
#
# q: Find the number of names which have a name score which is a triangle number
# a: 162
#

names_file = "data/p42_names.txt"
alph = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def name_score(name):
    score = 0
    for let in name: score += alph.index(let)
    return score

with open(names_file) as f:
    names = f.readline().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]

triangle_nums = set()
for i in range(0, 10000): triangle_nums.add(i*(i+1)/2)

ans = 0
for name in names:
    if name_score(name.lower()) in triangle_nums:
        ans += 1
print "p42: " + str(ans)

