# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 05:04:50 2020

@author: Rimpi
"""


string="hello"
reverse_String=reversed(string)
if list(string) == list(reverse_String):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
