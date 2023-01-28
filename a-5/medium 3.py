# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:54:43 2020

@author: Rimpi
"""


#medium-3

def invert_dict(d):
    dict={}
    for k,v in d.items():
        a=dict.setdefault(v,[])
        a.append(k)
       
    return dict   


