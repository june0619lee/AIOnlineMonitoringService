import grpc
import proto_sample_pb2, proto_sample_pb2_grpc
from concurrent import futures

import os
import argparse
import logging
from datetime import datetime

import numpy as np
from pytz import timezone

class StudyMonitoringModel(proto_sample_pb2_grpc.VirtualLearningMonitorServicer):
    def __init__(self, args):
        super().__init__()

        pass

        # TODO: implement

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='15011', help='server port. (defult:15011)')
    parser.add_argument('--logdir', type=str, default='./virtual_learning_log', help='directory to log file')
    parser.add_argument('--num_worker',type=int, default=4, help='the number of workers. (default:4)')

    return parser.parse_args()

def main():
    args = opt()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.num_worker))
    proto_sample_pb2_grpc.add_VirtualLearningMonitorServicer_to_server(StudyMonitoringModel(args), server)

    # port setting
    server.add_insecure_[port('[::]{}'.format(args.port))]
    # server start
    server.start
    # server 247 run
    server.wait_for_termination()


if __name__ == '__main__':
    main()