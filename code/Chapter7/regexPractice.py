#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:35:46 2019

@author: zhoutianbin
"""

"""
You can also use the pipe to match one of several patterns as part of your regex. 
For example, say you wanted to match any of the strings 'Batman', 
'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat, 
it would be nice if you could specify that prefix only once. 
This can be done with parentheses. 
"""

import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile Batbat  lost a wheel')
print(mo.group())
print(mo.group(1))
