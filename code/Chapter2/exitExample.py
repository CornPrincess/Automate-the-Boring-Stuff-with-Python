#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:10:34 2019

@author: zhoutianbin
"""

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')