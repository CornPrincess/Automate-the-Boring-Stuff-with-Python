#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:44:54 2019

@author: zhoutianbin
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidth = [0] * len(tableData)

for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        if len(tableData[i][j]) > colWidth[i]:
            colWidth[i] = len(tableData[i][j])
            
for i2 in range(len(tableData[0])):
    for j2 in range(len(tableData)):
        print(tableData[j2][i2].rjust(colWidth[j2]), end=' ')
    print()