#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:27:35 2019

@author: zhoutianbin

pw.py - An insecure password locker program
"""
import sys, pyperclip

PASSWORDS = {'email':'SSDFsdf56%^2356',
             'blog':'dsdfsdWERWERFSDG',
             'luggage':'sdfsd23423'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

print(sys.argv)
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)