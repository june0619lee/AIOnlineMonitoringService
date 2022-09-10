import grpc
import proto_sample_pb2, proto_sample_pb2_grpc
from concurrent import futures

import os
import argparse
import logging
from datetime import datetime

import numpy as np
from pytz import timezone

from ai_module import GazeTracker

class StudyMonitoringModel(proto_sample_pb2_grpc.AI_OnlineMonitoringServiceServicer):
    def __init__(self, args):
        super().__init__()

        if not os.path.exists(args.logdir):
            os.makedirs(args.logdir) # mkdir

        logdir = os.path.join(args.logdir, __class__.__name__+'.log')

        self.logger = logging.getLogger(__class__.__name__)
        self.logger.setLevel(logging.INFO)

        self.stream_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler(logdir)
        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.file_handler)

        self.fmt = "%Y-%m-%d %H:%M:%S"
        self.logger.info('{} server is ready to receive'.format(
            datetime.now(timezone('Asia/Seoul')).strftime(self.fmt)
        ))

        self.monitor_image = GazeTracker()

    def process(self, input, context):

        image = np.array(list(input.img_bytes))
        image = image.reshape((input.height, input.width, input.channel))
        image = np.array(image, dtype=np.uint8)

        return_data = proto_sample_pb2.ReturnData()

        try:
            result = self.monitor_image(image)
        except Exception as e:
            self.logger.info('{} error occurred {}'.format(
                datetime.now(timezone('Asia/Seoul')).strftime(self.fmt), e
            ))
            return_data.distance = -1
            return_data.face_yaw = -1.0
            return_data.eye_yaw = -1.0
        except KeyboardInterrupt:
            print("server terminated")
        else:
            return_data.distance = result.face_distance
            return_data.face_yaw = result.face_yaw
            return_data.eye_yaw = result.eye_yaw
        finally:
            self.logger.info('{} replying to client {}'.format(
                datetime.now(timezone('Asia/Seoul')).strftime(self.fmt), return_data.distance
            ))
            return return_data

            

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='16011', help='server port. (defult:15011)')
    parser.add_argument('--logdir', type=str, default='./virtual_learning_log', help='directory to log file')
    parser.add_argument('--num_worker',type=int, default=4, help='the number of workers. (default:4)')

    return parser.parse_args()

def main():
    args = opt()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.num_worker))
    proto_sample_pb2_grpc.add_AI_OnlineMonitoringServiceServicer_to_server(StudyMonitoringModel(args), server)

    # port setting
    server.add_insecure_port('[::]:{}'.format(args.port))
    # server start
    server.start
    # server 247 run
    server.wait_for_termination()


if __name__ == '__main__':
    main()