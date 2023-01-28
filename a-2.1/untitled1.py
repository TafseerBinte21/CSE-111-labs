# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:11:06 2020

@author: Rimpi
"""


def dom(x,y,z=" "):
    a=x[:x.find("@")]
    b=a[a.find("@")+1::]
    if b==x:
        print("unchanged= "+x)
    else:
        print("changed: "+a+"@"+y)
dom(input("enter email:"),input("new domain:")  )          