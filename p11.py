#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 11
#
# q: Find the largest product of 4 adjacent numbers in a grid 
# a: 70600674
#

file_name = 'data/p11_grid.txt'

f = open(file_name, 'r')
grid = []
for line in f: 
    row = []
    for num in line[:-1].split():
        row.append(int(num))
    grid.append(row)

def down(i,j):
    if i + 3 >= len(grid): return 0
    else: return grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]

def across(i,j):
    if j + 3 >= len(grid[i]): return 0
    else: return grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

def up_diag(i,j):
    if i - 3 < 0 or j + 3 >= len(grid[i]): return 0
    else: return grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]

def down_diag(i,j):
    if i + 3 >= len(grid) or j + 3 >= len(grid[i]): return 0
    else: return grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]

ans = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        ans = max(ans, max(down(i,j), max(across(i,j), max(down_diag(i,j), up_diag(i,j)))))

print "p11: " + str(ans)


