# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: str_or_repr.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/6 上午9:45

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/6 上午9:45
"""

"""
    __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
        ①打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。
        ②__repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。
    它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
"""


class Test(object):
    def __init__(self, value='Hello World!'):
        self.data = value


class TestStr(Test):
    def __str__(self):
        return '[Str_Value: %s]' % self.data


class TestRepr(Test):
    def __repr__(self):
        return '[Repr_Value: %s]' % self.data


if __name__ == '__main__':
    ts = TestStr()
    tr = TestRepr()
    print(ts)
    print(tr)
