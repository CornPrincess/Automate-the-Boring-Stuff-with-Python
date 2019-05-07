#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:13:51 2019

@author: zhoutianbin
"""

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'