# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: client.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/7/11 下午5:23

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/7/11 下午5:23
"""

import grpc
from gRPC import data_pb2_grpc, data_pb2

_HOST = '127.0.0.1'
_PORT = '5000'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.DataResponse(text='hello world'))
    print('Received:' + response.message)


if __name__ == '__main__':
    run()
