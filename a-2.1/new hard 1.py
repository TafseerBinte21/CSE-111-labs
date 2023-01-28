# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:48:40 2020

@author: Rimpi
"""


#hard task-1
import datetime
def bonusCount(*msalary):
    
    for i in range(0,len(msalary),3):
        bonus=0
        name=msalary[i]
        salary=int(msalary[i+1])
        
        joiningDate=int(msalary[i+2].split("-")[0])
        timeNow=datetime.datetime.now().year
        yearservice=timeNow-joiningDate
     
        if yearservice<5:
           bonus=int(10/100*salary)
        elif yearservice<=10:
           bonus=int((10/100*salary)+5000)
        else:
           bonus=int((15/100*salary+15000))
        if i== len(msalary)-3:   
            print(name+":",bonus)
        else:
            print(name+":" ,bonus,end=", ") 
bonusCount('Alice', 20000, '2017-03-21')             
bonusCount('Alice', 20000, '2017-03-21', 'Bob', 50000, '2007-05-10')

      
     
