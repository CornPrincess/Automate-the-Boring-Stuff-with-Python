#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:21:41 2019

@author: zhoutianbin
"""

def spam():
    global eggs
    eggs = 'spam'
    
def bacon():
    eggs = 'bacon'
    
def ham():
    print(eggs)

eggs = 42
ham()
bacon()
spam()
print(eggs)