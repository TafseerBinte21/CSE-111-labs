# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:06:00 2020

@author: Rimpi
"""


string = input('Enter string: ')
new_string = ''
new_string += string[0].upper()
i = 1

while i < len(string)-2:
    new_string += string[i]
    if string[i] == '.' or string[i] == '?' or string[i] == '!':
        new_string += ' '
        new_string += string[i+2].upper()
        i = i+3
    else:
        if i == len(string)-3:
            new_string += string[len(string)-2:len(string)]
        i = i+1

print(new_string)