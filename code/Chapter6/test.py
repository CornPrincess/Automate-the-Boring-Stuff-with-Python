#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:01:37 2019

@author: zhoutianbin
"""

#total = 0
#for num in range(101):
#    total += num
#print(total)

#for i in range(0, 10, 2):
#    print(i)

#for i in range(5, -1, -1):
#    print(i)

#def spam():
#    eggs = 31337
#
#spam()
#print(eggs)

#def spam():
#    eggs = 99
#    bacon()
#    print(eggs)
#
#def bacon():
#    ham = 101
#    eggs = 0
#
#a = 100 
#
#spam()

#def spam():
#    print(eggs)
#eggs = 42
#spam()
#print(eggs)

#def spam():
#    print(eggs)
#    eggs = 'spam local'
#    
#eggs = 'global'
#spam()

def spam(*argv):
    for i in argv:
        print(i)
        
a = [1,2,3,4]
spam(a)
spam(1,2,3,4)