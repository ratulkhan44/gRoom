import grpc
from concurrent import futures
import time 
from protos import groom_pb2_grpc as pb2_grpc
from protos import groom_pb2 as pb2
import random
import logging

class GroomService(pb2_grpc.GroomServicer):
    def __init__(self,*args, **kwargs):
        pass
    
    def get_room_number(self):
        return random.randint(1,101)
    
    def RegisterToRoom(self,request,context):
        try:
            print("========== Service Called =========")
            room_number = self.get_room_number()

            return pb2.RoomRegistrationResponse(room_id=room_number)
        except Exception as e:
            print("*********** Here is the Error ************",e.args[0])
    
    
def serve():
    try:
        port = "50051"
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_GroomServicer_to_server(GroomService(), server)
        server.add_insecure_port(f"[::]:{port}")
        server.start()
        print(f"Server started, listening on {port}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    logging.basicConfig()
    serve()