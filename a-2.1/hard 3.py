# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 08:44:49 2020

@author: Rimpi
"""

#hard task-3
def FixTheSentence(i):
    i = i.capitalize()
    length = len(i)
    b = 0
    newString= ""

    for n in range(length):

        if (b == 1 and i[n]!=' '):
            #print(i[n].capitalize())
            newString += i[n].capitalize()
            b = 0

        elif (i[n] == ' ' and n != 0):
            if (i[n - 1] == '?' or i[n - 1] == '!' or i[n - 1] == '.'):
                newString += i[n]
                b = 1

            else:
                newString += i[n]

        elif (n != length - 1 and i[n] == '.'):
            b = 1
            #print(i[n])
            newString += i[n]

        elif (n != length - 1 and i[n] == '?'):
            b = 1
            #print(i[n])
            newString += i[n]

        elif (n != length - 1 and i[n] == '!'):
            b = 1
            #print(i[n])
            newString += i[n]

        elif (n != length - 1 and i[n] == 'i'):
            if (i[n - 1] == ' ' and i[n + 1] == ' '):
                #print(i[n].capitalize())
                newString += i[n].capitalize()
            else:
                #print(i[n])
                newString += i[n]



        else:
            #print(i[n])
            newString += i[n]

    return newString

inputString = input()
print(FixTheSentence(inputString))
