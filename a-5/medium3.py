# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:45:38 2020

@author: Rimpi
"""


def invertdict(d):
    inv = {}
    for k, v in d.items():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv

print(invertdict({'key1': 'value1', 'key2': 'value2', 'key3': "value1"}))
