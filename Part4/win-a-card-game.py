# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:00:54 2021

@author: BjornN
"""

import seaborn as sns
import numpy as np
from scipy import stats

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
freq_winners = []
for _ in range(10_000):
    winners = []
    threshold2 = np.random.choice([13,14,16,17])
    for _ in range(1_000):
        winners.append(duel_play(15,threshold2))
    freq_winners.append(winners.count(15)/(1000-winners.count(0)))

sns.histplot(freq_winners)
freq_mean, freq_sigma = np.mean(freq_winners), np.std(freq_winners)
stats.norm.interval(0.95,loc=freq_mean,scale=freq_sigma/np.sqrt(len(freq_winners)))

