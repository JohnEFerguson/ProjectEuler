#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 22
#
# q: Sort a list of names and then calculate the sum of all of the names multiplied by their index in the sorted list
# a: 871198282
#

from helpers.sorting import merge_sort

names_file = "data/p22_names.txt"
alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def name_score(name):
    score = 0
    for let in name: score += alph.index(let)
    return score

with open(names_file) as f:
    names = f.readline().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]

sorted_names = merge_sort(names)
ans = 0
for i in range(0, len(sorted_names)):
    ans += (i+1) * name_score(sorted_names[i].lower())

print "p22: " + str(ans)

