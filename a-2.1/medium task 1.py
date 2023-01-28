# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:47:01 2020

@author: Rimpi
"""


def food(menu,place="mohakhali"):
    if place=="mohakhali":
       if menu=="beef burger":
          total=170+40+(8/100*170)
       elif menu=="bbq chicken cheese burger":
           total=250+40+(8/100*170)
       else:
            total=200+40+(8/100*170)
    else:
       if menu=="beef burger":
          total=170+60+(8/100*170)
       elif menu=="bbq chicken cheese burger":
           total=250+60+(8/100*170)
       else:
            total=200+60+(8/100*170)
    return total 
print(food("beef burger","mogbazar"))      

        
   