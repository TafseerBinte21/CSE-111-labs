# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:10:58 2020

@author: Rimpi
"""

mylist=[]
n=int(input("enter num:"))
for i in range(n):
    numbers = int(input('Enter number: '))
    mylist.append(numbers)

def countFre(mylist):
    freq={}
    for items in mylist:
        freq[items]=mylist.count(items)
    for key, value in freq.items():
        
       
        print ("% d - % d"%(key, value),'times')
countFre(mylist)        