# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:31:25 2020

@author: Rimpi
"""


def Vowel(a):
	return a.upper() in ['A', 'E', 'I', 'O', 'U'] 
def countV(string): 
    c=0
    v=" "
    for i in range(len(string)): 
        if Vowel(string[i]):
           c=c+1
    
           v=v+string[i]+","
    if c>0:
         print("vowels=" ,v,end=" ")
         print("Total vowels in string=",c)
    else:
          print("no vowels in string")
string="STEVE JOBS"         
print(countV(string))      
  