# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 07:32:09 2020

@author: Rimpi
"""

#hard task 1
from datetime import date  
def bonus(name,mSalary,yearservice): 
    dateTime=input()
    year=int(dateTime[:dateTime.find("-")])
    mNow=dateTime[dateTime.find("-")+1::]
    month=int(mNow[:mNow.find("-")])
    day=int(mNow[mNow.find("-")+1::])      
    d_year=365.2425
   

     
    if yearservice<5:
       bonus=(10/100*mSalary)
    elif yearservice>=5 and yearservice<=10:
        bonus=((10/100*mSalary)+5000)
    else:
        bonus=((15/100*mSalary+15000))
    return bonus
    print(name+":",bonus)
    yearservice=int((date.now()-date(year,month,day)).days/d_year)
a=input("enter name") 
s=int(input("enter salary"))
yS=int()  
bonus(a,s,yS)    
     

     