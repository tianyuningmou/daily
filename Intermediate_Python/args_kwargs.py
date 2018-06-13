# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: args_kwargs.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/6/13 下午2:25

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/6/13 下午2:25
"""

"""
    *args是用来发送一个非键值对的可变数量的参数列表给一个函数
    **kwargs允许你将不定长度的键值对,作为参数传递给一个函数 
    它也可以用来做猴子补丁(monkey patching)，猴子补丁的意思是在程序运行时(runtime)修改某些代码  
"""


def use_var_args(f_arg, *args):
    print('first normal args:', f_arg)
    for arg in args:
        print('another arg through *args:', arg)


use_var_args('python', 'eggs', 'birds', 'dogs')


def greet(**kwargs):
    for key, value in kwargs.items():
        print('{0}=={1}'.format(key, value))


greet(name='python')
