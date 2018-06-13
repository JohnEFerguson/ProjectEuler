#!/usr/bin/env python

#
# Jack Ferguson 2018
#
# Problem 54
#
# q: Find how many times player 1 wins the poker hand
# a: 376
#
# this could be SO MUCH BETTER please change eventually

rank = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}

def is_flush(hand):
    suit = hand[0][1]
    for c in hand:
        if c[1] != suit: return False
    return True

def is_straight(hand):
    min_rank = 13 # one more than the highest rank to start
    ranks = set()
    for c in hand:
        r = rank[c[0]]
        ranks.add(r)
        if r < min_rank: min_rank = r
    for i in range(1,5):
        if min_rank + i not in ranks: return [False, 0]
    return [True, min_rank]

def is_fullhouse(hand):
    trio = find_trio(hand)
    return [trio[0] and find_pair(trio[2])[0], high_card_value(hand)]

def is_royal_flush(hand):
    return is_flush(hand) and is_straight(hand)[0] and is_straight(hand)[1] == 8

def is_straight_flush(hand):
    return [is_flush(hand) and is_straight(hand)[0], is_straight(hand)[1]]

def is_foursome(hand):
    pair = find_pair(hand)
    other_pair = []
    if pair[0]: other_pair = find_pair([pair[2]])
    else: return [False, 0]
    return [pair[0] and other_pair[0] and pair[1] == other_pair[1], pair[1]]

def find_pair(hand): # return is_pair, rank of pair, remaining cards
    hand_copy = [c for c in hand]
    for i in range(0, len(hand)):
        for j in range(i+1, len(hand)):
            if rank[hand[i][0]] == rank[hand[j][0]]: # found
                ans = [True, rank[hand[i][0]]]
                hand_copy.pop(i)
                hand_copy.pop(j-1)
                return ans + [hand_copy]
    return [False, 0, hand_copy] # not found

def has_two_pairs(hand):
    pair1 = find_pair(hand)
    if not pair1[0]: return [False, 0]
    else:
        pair2 = find_pair(pair1[2])
        return [pair2[0], max(pair1[1], pair2[1]), pair2[2]]

def find_trio(hand):
    hand_copy = [c for c in hand]
    for i in range(0, len(hand)-2):
        for j in range(i+1, len(hand)-1):
            for k in range(j + 1, len(hand)):
                if rank[hand[i][0]] == rank[hand[j][0]] and rank[hand[j][0]] == rank[hand[k][0]]:
                    ans = [True, rank[hand[i][0]]]
                    hand_copy.pop(i)
                    hand_copy.pop(j-1)
                    hand_copy.pop(k-2)
                    return ans + [hand_copy]
    return [False, 0, hand_copy]

def high_card_value(hand):
    max_val = 0
    for c in hand:
        if rank[c[0]] > max_val: max_val = rank[c[0]]
    return max_val

def find_winner(h1, h2):
    if is_royal_flush(h1): 
        return 1
    elif is_royal_flush(h2): 
        return 2
    elif is_straight_flush(h1)[0]:
        if is_straight_flush(h2)[0]:
            if high_card_value(h1) > high_card_value(h2): 
                return 1 # WHAT IF SAME?
            else: 
                return 2 
        else: 
            return 1
    elif is_straight_flush(h2)[0]: 
            return 2
    elif is_foursome(h1)[0]:
        if is_foursome(h2)[0]:
            if high_card_value(h1) > high_card_value(h2): 
                return 1 # WHAT IF SAME?
            else: 
                return 2 
    elif is_foursome(h2)[0]:
        return 2
    elif is_fullhouse(h1)[0]:
        if is_fullhouse(h2)[0]:
            if high_card_value(h1) > high_card_value(h2): 
                return 1 # WHAT IF SAME?
            else: 
                return 2 
        else: 
            return 1
    elif is_fullhouse(h2)[0]: 
        return 2
    elif is_flush(h1):
        if is_flush(h2):
            if high_card_value(h1) > high_card_value(h2): 
                return 1 # WHAT IF SAME?
            else: 
                return 2 
        else:
            return 1
    elif is_flush(h2): 
        return 2
    elif is_straight(h1)[0]:
        if is_straight(h2)[0]:
            if high_card_value(h1) > high_card_value(h2): 
                return 1 # WHAT IF SAME?
            else: 
                return 2 
        else: 
            return 1
    elif is_straight(h2)[0]: 
        return 2
    elif find_trio(h1)[0]:
        if find_trio(h2)[0]:
            if find_trio(h1)[1] > find_trio(h2)[1]: 
                return 1
            elif find_trio(h1)[1] == find_trio(h2)[1]:
                if high_card_value(find_trio(h1)[2]) > high_card_value(find_trio(h2)[2]): 
                    return 1 # WHAT IF SAME?
                else: 
                    return 2 
            else: 
                return 2 
        else: 
            return 1
    elif find_trio(h2)[0]:
        return 2
    elif has_two_pairs(h1)[0]:
        if has_two_pairs(h2)[0]:
            if has_two_pairs(h1)[1] > has_two_pairs(h2)[1]: 
                return 1
            elif has_two_pairs(h1)[1] == has_two_pairs(h2)[1]:
                if has_two_pairs(h1)[2][0] > has_two_pairs(h2)[2][0]:
                    return 1 # WHAT IF SAME?
                else: 
                    return 2 
            else: 
                return 2 
        else: 
            return 1
    elif has_two_pairs(h2)[0]: 
        return 2
    elif find_pair(h1)[0]:
        if find_pair(h2)[0]:
            if find_pair(h1)[1] > find_pair(h2)[1]: 
                return 1
            elif find_pair(h1)[1] == find_pair(h2)[1]:
                if high_card_value(find_pair(h1)[2]) > high_card_value(find_pair(h2)[2]):
                    return 1 # WHAT IF SAME?
                else: 
                    return 2 
            else: 
                return 2 
        else: 
            return 1
    elif find_pair(h2)[0]: 
        return 2
    elif high_card_value(h1) > high_card_value(h2): 
        return 1 # WHAT IF SAME?
    else: return 2 
    


file_name = "data/p54_poker.txt"
p1_hands = []
p2_hands = []
ans = 0
f = open(file_name, 'r')
for line in f:
    p1_hands.append(line[:-1].split(" ")[:5])
    p2_hands.append(line[:-1].split(" ")[5:])

for i in range(0, len(p1_hands)):
    if find_winner(p1_hands[i], p2_hands[i]) == 1:
        ans += 1
print 'p54: ' + str(ans)

