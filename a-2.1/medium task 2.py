# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:28:15 2020

@author: Rimpi
"""


def dom(x,y,z=None):
    m=x[:x.find("@")]
    n=x[x.find("@")+1::]
    if n==m:
        print("unchanged= "+x)
    else:
        print("changed: "+m+"@"+y)
dom(input("mail:"),input("new domain:"),input())            