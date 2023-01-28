# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 00:19:38 2020

@author: Rimpi
"""


def Vowel(a):
    return a.upper() in ['A','E','I','O','U']
 
    #ekhane upper korteso but original string
    #ta kintu change hoye jacche
 
def countV(string):
    c=0
    v=""
 
 
    for i in range (len(string)):
        if Vowel(string[i]):
 
            v=v+string[i]+","
            c+=1
 
    if c==0:
        print("no vowels in string")
    else:
 
        old = v
        new_list = list(v)
        new_list[len(v)-1] = "."
        new = "".join(new_list)
 
        print("Vowels:" +new)
        print("Total vowels in strings=",c)
 
string ="STEVE JOBS"
countV(string)# your code goes here