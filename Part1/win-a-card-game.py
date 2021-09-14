# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:00:54 2021

@author: BjornN
"""

# Type 2
import seaborn as sns

x = [x for x in [2,3,4,5,6,7,8,9,10,10,10,10,11] for y in [1,2,3,4]]
len(x)

sns.histplot(x,discrete=True)

