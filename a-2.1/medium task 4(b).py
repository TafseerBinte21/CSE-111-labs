# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 05:14:45 2020

@author: Rimpi
"""

def palindrome(s): 

    a=s[::-1]
    if s==a:
       print("TRUE")
    else:
       print("FALSE")

s=input("enter a string:") 
palindrome(s)      