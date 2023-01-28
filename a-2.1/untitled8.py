# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:30:32 2020

@author: Rimpi
"""


string = input("Enter a string: ")
if string == 's':
    exit()
else:
    newstr = string
    print("\nRemoving vowels from the given string")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for s in string.lower():
        if s in vowels:
           newstr = newstr.replace(s,"")
 
    print("New string after successfully removed all the vowels:")
    print(newstr)