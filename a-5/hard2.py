# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:38:09 2020

@author: Rimpi
"""


#hard2
d = {}
d[1] = ".,?!:"
d[2] = "ABC"
d[3] = "DEF"
d[4] = "GHI"
d[5] = "JKL"
d[6] = "MNO"
d[7] = "PQRS"
d[8] = "TUV"
d[9] = "WXYZ"
d[0] = " "

s=input("enter msg:")
for i in s:
    for k,v in s.items():
        if i in v:
            for j in range(v[i]):
                print(k)
            
    