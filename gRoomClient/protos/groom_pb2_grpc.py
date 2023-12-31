# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import groom_pb2 as protos_dot_groom__pb2


class GroomStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterToRoom = channel.unary_unary(
                '/groom.Groom/RegisterToRoom',
                request_serializer=protos_dot_groom__pb2.RoomRegistrationRequest.SerializeToString,
                response_deserializer=protos_dot_groom__pb2.RoomRegistrationResponse.FromString,
                )


class GroomServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterToRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroomServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterToRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterToRoom,
                    request_deserializer=protos_dot_groom__pb2.RoomRegistrationRequest.FromString,
                    response_serializer=protos_dot_groom__pb2.RoomRegistrationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'groom.Groom', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Groom(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterToRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/groom.Groom/RegisterToRoom',
            protos_dot_groom__pb2.RoomRegistrationRequest.SerializeToString,
            protos_dot_groom__pb2.RoomRegistrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
