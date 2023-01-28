# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:13:12 2020

@author: Rimpi
"""


#easy-3
my_dict={}
i=0
while i<10:
    num=int(input("enter a number:"))
    if my_dict.get(num):
        my_dict[num]=1
        i+=1
    else:
        print('Duplicate')
for i in my_dict:
    print(i, end=' ')
        
        