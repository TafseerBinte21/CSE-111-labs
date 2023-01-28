# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:36:59 2020

@author: Rimpi
"""



def many(min,max,div):
    
    c=0
    for i in range(min,max):
        if i%div==0:
           c+=i  
    return c
    
print(many(0,10,2))  
    
   