# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:00:54 2021

@author: BjornN
"""

import seaborn as sns
import numpy as np

def tryUnbust(hand):
    for idx,val in enumerate(hand):
        if val == 11:
            hand[idx] = 1
            break
    return hand

np.random.seed(0)
deck = [x for x in [2,3,4,5,6,7,8,9,10,10,10,10,11] for y in [1,2,3,4]]
npdeck = np.array(deck)
results = np.zeros((100_000), dtype=int)
debug = True
for i in range(0,100_000):
#    np.random.shuffle(npdeck)
    npdeck = np.random.permutation(np.array(deck))
    hand = npdeck[:2]
#    print(f"Starting new hand {hand}") 
    hand_idx = 2
    if (sum(hand) >= 22):
        hand = tryUnbust(hand)
#    print(f"Sum: {sum(hand)}") 
    while (sum(hand) < 16):
#        print(f"Picking {npdeck[hand_idx]}") 
        hand = np.append(hand, [npdeck[hand_idx]])            
#        print(f"Sum: {sum(hand)}") 
        if (sum(hand) >= 22):
            hand = tryUnbust(hand)            
        hand_idx += 1
    results[i] = sum(hand)
    

sns.histplot(results)


