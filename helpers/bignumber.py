#!/usr/bin/env python

class BigNumber:
    def __init__(self, n):
        self.number = []
        for dig in str(n)[::-1]:
            self.number.append(int(dig))
    def length(self): return len(self.number)
    def add(self, n):
        if self.length() > n.length(): n.extend(self.length())
        elif self.length() < n.length(): self.extend(n.length())
        carry = 0
        for i in range(0, self.length()):
            num = self.number[i] + n.get(i) + carry
            if num >= 10: 
                carry = 1
                num -= 10
            else: carry = 0
            self.number[i] = num
            if i == self.length() - 1 and carry == 1:
                self.number.append(1)

    def multiply(self, n):
        #if self.length() > n.length(): n.extend(self.length())
        #elif self.length() < n.length(): self.extend(n.length())
        nums = []

        carry = 0
        for i in range(0, self.length()):
            num = ''.join((['0']*i))
            for j in range(0, n.length()):
                dig = int(self.get(i)) * int(n.get(j)) + carry
                if dig >= 10 and j != n.length() - 1: 
                    carry = 1
                    dig -= 10
                else: carry = 0
                num = str(dig) + num
            nums.append(BigNumber(int(num)))
        self.number = nums[0].number
        for num in nums[1:]:
            self.add(num)

    def multiply(self, n, small): # this one is noticeably faster
        this = BigNumber(str(self))
        for i in range(0, n-1):
            self.add(this)
            
    def extend(self, new_length):
        while self.length() < new_length: self.number.append(0)
    def pow(self, n):
        self.pow_helper(n, BigNumber(str(self)))
    def pow_helper(self, n, this):
        while n > 1:
            #self.multiply(this)
            self.multiply(int(str(this)), ' ')
            n -= 1
    def get(self, i): return self.number[i]
    def __str__(self): 
        return ''.join([str(x) for x in self.number[::-1]])

