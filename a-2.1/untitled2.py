# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 07:57:15 2020

@author: Rimpi
"""


def time(no_days):
    years=int(no_days/365)
    days=(no_days%365)
    months=(days//30)
    days=days%30
    print(years,"Year",months,"Month",days,"Days")
no_days =4320
time(no_days)
    
    
    