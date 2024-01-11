from concurrent import futures
import logging

import grpc
from server.time import time_pb2, time_pb2_grpc

class TimeServicer(time_pb2_grpc.TimeServicer):
    def GetDatetime(self, request, context):
        date_time = time_pb2.Datetime()
        date_time.ms = request.ms
        date_time.iso = "2020-02-14T10:10:10.123456Z"
        return date_time

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    time_pb2_grpc.add_TimeServicer_to_server(TimeServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()