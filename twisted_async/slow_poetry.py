# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: slow_poetry.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/6/21 下午3:27

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/6/21 下午3:27
"""

import optparse, os, socket, time


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('--port', type='int')
    parser.add_option('--iface', default='localhost')
    parser.add_option('--delay', type='float', default=.7)
    parser.add_option('--num-bytes', type='int', default=10)

    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('Provide exactly one poetry file')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parser.error('No such file: %s'.format(args[0]))

    return options, poetry_file


def send_poetry(sock, poetry_file, num_bytes, delay):
    inputf = open(poetry_file, 'r')
    
