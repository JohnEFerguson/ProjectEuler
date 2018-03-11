#!/usr/bin/env python

#
# Jack Ferguson 2017
#
# Problem 1
#
# q: Find the number of the characters in the numbers [1,1000] written in english
# a: 21124
#

from __future__ import division

first = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
then = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

ans = len('onethousand')
for n in range(0, 1000):
    if n >= 100:
        c = n/100
        if float(c).is_integer(): ans += len('hundred')
        else: 
            ans += len("hundredand")
        c = int(c)
        ans += len(first[c])
        n -= c*100
    if n > 19:
        c = int(n/10)
        ans += len(then[c])
        n -= c*10
    ans += len(first[n])
print "p17: " + str(ans)

    
    
