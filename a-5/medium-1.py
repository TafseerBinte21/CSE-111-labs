# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:47:41 2020

@author: Rimpi
"""
#medium-1
d1={'a': 100, 'b': 100, 'c': 200, 'd': 300}
d2={'a': 300, 'b': 200, 'd': 400, 'e': 200}

for key in d2: 
    if key in d1: 
        d2[key] = d2[key] + d1[key] 
    else: 
        pass
          
print(d2) 
