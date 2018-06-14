# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: map_filter_reduce.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/6/14 下午3:56

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/6/14 下午3:56
"""

from functools import reduce

items = [1, 2, 3, 4, 5]
squared = []
for item in items:
    squared.append(item ** 2)
print(squared)

map_squared = list(map(lambda item: item ** 2, items))
print(map_squared)


number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))


product = reduce((lambda x, y: (x * y)), [1, 2, 3, 4])
print(product)
