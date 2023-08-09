import grpc
from concurrent import futures
import time 
from protos import groom_pb2_grpc as pb2_grpc
from protos import groom_pb2 as pb2
import logging


class GroomClient:
    def __init__(self) -> None:
        self.host = "localhost"
        self.server_port = "50051"
        
        self.channel = grpc.insecure_channel("{}:{}".format(self.host,self.server_port))
        
        self.stub = pb2_grpc.GroomStub(self.channel)
        
    
    def get_room_id(self,room_name):
        
        room_name = pb2.RoomRegistrationRequest(room_name=room_name)
        
        return self.stub.RegisterToRoom(room_name)
        
        
if __name__== '__main__':
    client = GroomClient()
    
    for i in range(10000):
        print("+++++++++++ ",i)
        room_name = f"My_Room_{i}"
    
        response = client.get_room_id(room_name=room_name)
        print("********* Here is response ************",response)
    
    
        
        
        



