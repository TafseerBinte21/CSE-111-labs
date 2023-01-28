# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:04:09 2020

@author: Rimpi
"""

h=input("enter h=")
w=input("enter w=")
h=float(h)
w=float(w)
convert = h/100
def anyThing(h,w):
       
    score=w/(convert*convert)
    score="{:.2f}".format(score)
    score=float(score)
    if score<18.5:
       print ("Underweight")
    elif score>=18.5 and score<=24.9:
        print ("Normal")
    elif score>=25 and score<=30:
        print ("Overweight")
    else:
        print("obese")
    print("score is:",score)
anyThing(convert,w)   