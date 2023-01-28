# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:07:56 2020

@author: Rimpi
"""


  
def bonus(*a):
    import datetime      
    for i in range(0,len(a),3):
        bonus:0
        name:a[i]
        mSalary:a[i+1]
        
        joiningDate=int(a[i+2].split("-"))
        timeNow=datetime.datetime.now().year
        yearservice=((timeNow)-(joiningDate/365))
   
        
     
        if yearservice<5:
           bonus=(10/100*a)
        elif yearservice>=5 and yearservice<=10:
           bonus=((10/100*a)+5000)
        else:
           bonus=((15/100*a+15000))
        if i== len(a)-3:   
    
           print(f"{name}: {bonus}")
        else:
           print(f"{name}: {bonus}",end=", ") 

      
     

     