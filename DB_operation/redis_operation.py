# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: redis_operation.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/10 下午2:21

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/10 下午2:21
"""

import time
import redis

# 建立连接
redis_conn = redis.Redis()
#
# # 字符串存取
redis_conn.set('name', 'mongodb')
print(redis_conn.get('name'))

# 哈希存取
redis_conn.hset('db', 'nosql', 'redis')
print(redis_conn.hget('db', 'nosql'))

# 列表存取
redis_conn.lpush('nosql', 'redis', 'mongodb', 'redis')
redis_conn.lpop('nosql')
print(redis_conn.lrange('nosql', 0, 1))

redis_conn.sadd('no_sql', 'mongodb', 'redis')
print(redis_conn.smembers('no_sql'))


# 测试管道
def time_sum(func):
    def time_interval(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('spend time: {time} s'.format(time=end_time-start_time))
    return time_interval()


@time_sum
def without_pipeline():
    for i in range(100000):
        redis_conn.ping()


@time_sum
def with_pipeline():
    pipeline = redis_conn.pipeline(transaction=True)
    for i in range(100000):
        pipeline.ping()


if __name__ == '__main__':
    pass
