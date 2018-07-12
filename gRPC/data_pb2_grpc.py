# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class FormatDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoFormat = channel.unary_unary(
        '/data.FormatData/DoFormat',
        request_serializer=data__pb2.DataResponse.SerializeToString,
        response_deserializer=data__pb2.DataReplay.FromString,
        )


class FormatDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DoFormat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FormatDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoFormat': grpc.unary_unary_rpc_method_handler(
          servicer.DoFormat,
          request_deserializer=data__pb2.DataResponse.FromString,
          response_serializer=data__pb2.DataReplay.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'data.FormatData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
