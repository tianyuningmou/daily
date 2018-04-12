# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: magic_methods.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/12 下午12:07

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/12 下午12:07
"""

"""
构造和初始化:
    __new__:  生成实例时第一个调用的方法，用来创建类并返回这个类的实例，并且总是需要返回该类的一个实例
    __init__: 在对象初始化的时候调用，只是将传入的参数来初始化该实例，不能返回除了None的任何值。一般将它理解为"构造函数"
    __del__:  在对象生命周期结束时调用，此方法定义的是当一个对象进行垃圾回收时候的行为。一般将它理解为"析构函数"
属性访问控制:
    __getattr__: 该方法定义了你试图访问一个不存在的属性时的行为。因此，重载该方法可以实现捕获错误拼写然后进行重定向, 或者对一些废弃的属性进行警告
    __setattr__: 它定义了你对属性进行赋值和修改操作时的行为。不管对象的某个属性是否存在,它都允许你为该属性进行赋值,因此你可以为属性的值进行自定义操作
                 有一点需要注意，实现__setattr__时要避免"无限递归"的错误
    __delattr__: 它定义的是你删除属性时的行为。实现__delattr__是同时要避免"无限递归"的错误
描述器对象: 描述器对象不能独立存在, 它需要被另一个所有者类所持有。描述器对象可以访问到其拥有者实例的属性
           在面向对象编程时，如果一个类的属性有相互依赖的关系时，使用描述器来编写代码可以很巧妙的组织逻辑
    __get__: 在其拥有者对其读值的时候调用
    __set__: 在其拥有者对其进行修改值的时候调用
    __del__: 在其拥有者对其进行删除的时候调用
构造自定义容器: 
    如果要自定义不可变容器类型，只需要定义__len__ 和 __getitem__方法
    如果要自定义可变容器类型，还需要在不可变容器类型的基础上增加定义__setitem__ 和 __delitem__
    如果你希望你的自定义数据结构还支持"可迭代", 那就还需要定义__iter__
    __reversed__(self): 如果想要该数据结构被內建函数reversed()支持，就还需要实现该方法
    __contains__(self, item): 如果定义了该方法，那么在执行item in container 或者 item not in container时该方法就会被调用
                              如果没有定义，那么Python会迭代容器中的元素来一个一个比较，从而决定返回True或者False
    __missing__(self, key): dict字典类型会有该方法，它定义了key如果在容器中找不到时触发的行为
                            比如d = {'a': 1}, 当你执行d[not exist]时，d.__missing__['not exist']就会被调用
上下文管理:
    __enter__会返回一个值，并赋值给as关键词之后的变量。在这里，你可以定义代码段开始的一些操作
    __exit__(self, exception_type, exception_value, traceback)
        __exit__定义了代码段结束后的一些操作，可以这里执行一些清除操作，或者做一些代码段结束后需要立即执行的命令，比如文件的关闭，socket断开等
        如果代码段成功结束，那么exception_type, exception_value, traceback 三个参数传进来时都将为None
        如果代码段抛出异常，那么传进来的三个参数将分别为: 异常的类型，异常的值，异常的追踪栈
        如果__exit__返回True, 那么with声明下的代码段的一切异常将会被屏蔽
        如果__exit__返回None, 那么如果有异常，异常将正常抛出，这时候with的作用将不会显现出来
其它:
    __str__(self):  对实例使用str()时调用
    __repr__(self): 对实例使用repr()时调用。
        str()和repr()都是返回一个代表该实例的字符串，
        主要区别在于: str()的返回值要方便人来看，而repr()的返回值要方便计算机看。

    __unicode__(self): 对实例使用unicode()时调用。
        unicode()与str()的区别在于: 前者返回值是unicode，后者返回值是str。unicode和str都是basestring的子类。
        当你对一个类只定义了__str__但没定义__unicode__时，__unicode__会根据__str__的返回值自动实现，即return unicode(self.__str__())
"""
