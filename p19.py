#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 19
#
# q: How many Sundays fell on the first of the month in the 20th century
# a: 171
#

ans = 0
y = 1900
md = 1
wd = 1
m = 1
m_ranges = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
while y < 2001:
    if y%4 == 0: 
        m_ranges[1] = 29
    else: m_ranges[1] = 28
    m = 1
    while m <= 12:
        md = 1
        if wd == 7 and y > 1900: ans += 1
        while md <= m_ranges[m-1]:
            md += 1
            if wd == 7: 
                wd = 1
            else: wd += 1
        m += 1
    y += 1

print "p19: " + str(ans)

    
    
