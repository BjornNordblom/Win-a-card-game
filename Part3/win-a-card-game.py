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

def simulate_game(shuffled_deck, threshold):
    hand = shuffled_deck[:2]
    hand_idx = 2
    if (sum(hand) > 21):
        hand = tryUnbust(hand)
    while (sum(hand) < threshold):
        hand = np.append(hand, [shuffled_deck[hand_idx]])            
        if (sum(hand) > 21):
            hand = tryUnbust(hand)            
        hand_idx += 1
    return hand

def duel_play(threshold1, threshold2):
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    npdeck = np.random.permutation(np.array(deck))    
    p1 = simulate_game(npdeck, threshold1)
    p2 = simulate_game(npdeck[len(p1):], threshold2)
    if ((sum(p1) > sum(p2) and sum(p1) <= 21 and sum(p2) <= 21) or (sum(p1) <= 21 and sum(p2) > 21)):
        return threshold1
    elif ((sum(p2) > sum(p1) and sum(p2) <= 21 and sum(p1) <= 21) or (sum(p2) <= 21 and sum(p1) > 21)):
        return threshold2
    else:
        return 0

np.random.seed(0)
winners = []

for i in range(10_000):
    for threshold1 in range(10,20):
        for threshold2 in range(10,20):
            winners.append(duel_play(threshold1,threshold2))

sns.histplot(winners,discrete=True)


