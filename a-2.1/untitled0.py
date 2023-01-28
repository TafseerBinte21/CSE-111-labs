# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:12:41 2020

@author: Rimpi
"""


class Solution(object):
   def removeVowels(r,s):
      s = s.replace("a","")
      s = s.replace("e","")
      s = s.replace("i","")
      s = s.replace("o","")
      s = s.replace("u","")
      return s
ob1 = Solution()
s=input("enter a string")
print(s)
print(ob1.removeVowels(s))




