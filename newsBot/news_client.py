import grpc
from concurrent import futures
import time 
from protos import news_bot_pb2_grpc as pb2_grpc
from protos import news_bot_pb2 as pb2
import logging


class GroomClient:
    def __init__(self) -> None:
        self.host = "localhost"
        self.server_port = "50051"
        
        self.channel = grpc.insecure_channel("{}:{}".format(self.host,self.server_port))
        
        self.stub = pb2_grpc.GroomStub(self.channel)
        
    
    def get_news_status(self,news_item):
        
        news_item = pb2.NewsFlash(news_item=news_item)
        
        return self.stub.SendNewsStream(news_item)
        
        
if __name__== '__main__':
    try:
        client = GroomClient()
        
        for i in range(10000):
            print("+++++++++++ ",i)
            news_item = f"News_Item_{i}"
        
            response = client.get_news_status(news_item=
                    {
                        "news_time": {
                            "seconds": 20,
                            "nanos": 10
                        },
                        "news_item": "Hello"
                    }
                )
            print("********* Here is response ************",response)
            
    except Exception as e:
        print("********* Error ***********",e.args[0])
    
    
        
        
        



