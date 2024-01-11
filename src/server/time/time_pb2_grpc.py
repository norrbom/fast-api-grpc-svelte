# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from server.time import time_pb2 as server_dot_time_dot_time__pb2


class TimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDatetime = channel.unary_unary(
                '/time.Time/GetDatetime',
                request_serializer=server_dot_time_dot_time__pb2.Timestamp.SerializeToString,
                response_deserializer=server_dot_time_dot_time__pb2.Datetime.FromString,
                )


class TimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDatetime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDatetime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatetime,
                    request_deserializer=server_dot_time_dot_time__pb2.Timestamp.FromString,
                    response_serializer=server_dot_time_dot_time__pb2.Datetime.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'time.Time', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Time(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDatetime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/time.Time/GetDatetime',
            server_dot_time_dot_time__pb2.Timestamp.SerializeToString,
            server_dot_time_dot_time__pb2.Datetime.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
