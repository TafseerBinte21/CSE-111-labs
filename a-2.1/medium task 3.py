# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:33:06 2020

@author: Rimpi
"""

def Vowel(a): 
	return a.upper() in ['A', 'E', 'I', 'O', 'U'] 
def countV(string): 
    c=0
    v=" "
   
    for i in range(len(string)): 
        if Vowel(string[i]):
           v=v+string[i]+","
           c+=1       
           
           
    if c==0:
         print("no vowels in string")
    else:
        old=v
        newList=list(v)
        newList[len(v)-1]="."
        new="".join(newList)
        
        print("Vowels:" +new)
        print(" Total vowels in string=",c) 

string="STEVE JOBS"         
countV(string)     
  