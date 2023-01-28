# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:01:33 2020

@author: Rimpi
"""


#easy-2
my={'Physics': 82, 'Math' : 65, 'History': 75}
key_max=max(my, key=my.get)
key_min=min(my, key=my.get)

print('Minimum:',key_min)
print('Maximum:',key_max)