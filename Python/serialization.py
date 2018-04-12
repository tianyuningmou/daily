# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: serialization.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/9 下午12:09

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/9 下午12:09
"""

"""
    Pickle序列化：
        该模块实现了基本的数据序列化和反序列化，通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；
        通过pickle模块的反序列化操作，我们可以取得保存的数据。
    JSON序列化：
        json是一种轻量级的数据交换格式，易于阅读和编写。
    marshal序列化：
        marshal并不通用，因为使用marshal序列化的二进制数据格式还没有文档化。
"""

import marshal
import json
import pickle

origin_list = [1, (2, 'string'), {'key': 'value'}]

json_encode = json.dumps(origin_list)
json_decode = json.loads(json_encode)
print(json_decode)

with open('ser_file.marshal', 'wb') as file:
    marshal.dump(origin_list, file)

with open('ser_file.marshal', 'rb') as file:
    marshal_list = marshal.load(file)
    print(marshal_list)

with open('ser_file.txt', 'wb') as file:
    pickle.dump(origin_list, file)

with open('ser_file.txt', 'rb') as file:
    pickle_list = pickle.load(file)
    print(pickle_list)
