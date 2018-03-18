#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 18
#
# q: Find the maximum sum calculated by following a path on a triangle
# a: 1074
#

file_name = 'data/p18_triangle.txt'

f = open(file_name, 'r')
triangle = []
for line in f:
    row = []
    for num in line[:-1].split():
        row.append(int(num))
    triangle.append(row)

for i in range(len(triangle)-2, -1, -1):
    for j in range(0, len(triangle[i])):
        triangle[i][j] = max(triangle[i][j]+triangle[i+1][j], triangle[i][j]+triangle[i+1][j+1])

print "p18: " + str(triangle[0][0])

    
    
