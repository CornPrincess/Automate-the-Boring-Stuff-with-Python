#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:15:51 2019

@author: zhoutianbin
"""

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

#Paste text from the clipboard
#
#Do something to it
#
#Copy the new text to the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)
pyperclip.copy(text)

# =============================================================================
# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars
# 
# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars
# =============================================================================
