from helpers.divisors import get_divisors

all_digs = set()
for i in range(1, 10): all_digs.add(i)

def is_pandigital(s): 
    if len(s) != 9: return False
    digs = set()
    for dig in s: digs.add(int(dig))
    return digs == all_digs
    
def is_factor_pandigital(n):
    divisors = get_divisors(n)
    for div in divisors:
        digs = str(n)
        digs += str(div) + str(n/div)
        if is_pandigital(digs): return True
    return False

nums = []
def get_pandigital_nums_helper(so_far, left):
    if left == '' and so_far[0] != '0': nums.append(so_far)
    else:
        for i in range(0, len(left)): get_pandigital_nums_helper(so_far + left[i], left[:i] + left[i+1:])

def get_pandigital_nums(digs):
    get_pandigital_nums_helper('', digs)
    return nums
