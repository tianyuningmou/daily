# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: server.py.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/7/11 下午5:10

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/7/11 下午5:10
"""

import grpc
import time
from concurrent import futures
from gRPC import data_pb2, data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '5000'

class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = request.text
        return data_pb2.DataReplay(message=str.upper())


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
