#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:18:21 2019

@author: zhoutianbin
"""

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)