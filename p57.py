#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 57
#
# q: 
# a: 
#
#

def num_digits(n): return len(str(n))

series = [0,1,2,5,12,29]
while len(series) < 1000: series.append(series[-1]*2 + series[-3]*2 + series[-4])
ans = 0
for i in range(3, len(series)):
    if num_digits(series[i] + series[i-1]) > num_digits(series[i]):
        ans += 1
print 'p57: ' + str(ans)

