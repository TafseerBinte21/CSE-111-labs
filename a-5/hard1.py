# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:07:54 2020

@author: Rimpi
"""

#hard-1

a=input("enter a string:")
d={}
for i in a:
   if i in d:
       d[i]+=1
   else:
       d[i]=1
print(d)

b=input("enter a string:")
d1={}
for i in b:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)
    
if (sorted(d)==sorted(d1)):
    print("anagrams")
else:
    print("not anagrams")
    





    
