import grpc
import proto_sample_pb2, proto_sample_pb2_grpc
from concurrent import futures

import os
import argparse
import logging
from datetime import datetime

import numpy as np
from pytz import timezone

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='15011', help='server port. (defult:15011)')
    parser.add_argument('--logdir', type=str, default='./virtual_learning_log', help='directory to log file')
    parser.add_argument('--num_worker',type=int, default=4, help='the number of workers. (default:4)')

    return parser.parse_args()

def main():
    args = opt()

    print(args.port)
    print(args.logdir)
    print(args.num_worker)


if __name__ == '__main__':
    main()