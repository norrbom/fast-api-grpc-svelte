import logging
import grpc
from server.time import time_pb2, time_pb2_grpc

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

channel = grpc.insecure_channel('localhost:50051')
stub = time_pb2_grpc.TimeStub(channel)

date_time = stub.GetDatetime(time_pb2.Timestamp(ms=1234567890))
logger.debug(date_time)


