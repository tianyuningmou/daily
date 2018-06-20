# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: threading_condition.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/6/20 下午4:26

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/6/20 下午4:26
"""

import threading
import time


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            print(time.time())
            time.sleep(1)

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()


if __name__ == '__main__':
    job = Job()
    job.start()
    time.sleep(3)
    job.pause()
    time.sleep(3)
    job.resume()
    time.sleep(3)
    job.pause()
    time.sleep(2)
    job.stop()
