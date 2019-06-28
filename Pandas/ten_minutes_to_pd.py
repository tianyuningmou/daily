# -*- coding: utf-8 -*-

"""
Copyright () 2019

All rights reserved

FILE: ten_minutes_to_pd.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2019-06-28 11:52

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2019-06-28 11:52
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
    创建一个Series，pandas会自动创建一个整数索引
    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64
"""
series = pd.Series([1, 3, 5, np.nan, 6, 8])
print(series)

# 通过传递带有日期时间索引和带标签列的NumPy数组来创建DataFrame
dates = pd.date_range('2019-06-20', periods=10)
print(dates)

df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list('ABCD'))
print(df)
print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())

# 通过传递类似Series的dict对象来创建DataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190630'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
