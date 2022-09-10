from turtle import width
import grpc
import proto_sample_pb2
import proto_sample_pb2_grpc

import os
import cv2 # webcam control; image processing
import argparse
import random

class Feedback_message:
    message_dict = {
        'ok' : {
            'text' : 'okay',
            'color' : (0,255,0)
        },
        'close' : {
            'text' : 'WARNING: too close',
            'color' : (0,0,255)
        },
        'none' : {
            'text' : 'Server not found',
            'color' : (0,0,255)
        }
    }

def distance_based_feedback(distance, frame, thres_value=95):
    '''
        args:
            distance (int): face to monitor distance
            frame (np.ndarray): user's front webcam image
        return:
            frame (np.ndarray): annotated frame
    '''


    if distance == -1:
        key = 'none'
    elif distance < thres_value: # too close
        key = 'close'
        os.system('say too close') # tts
    else:
        key = 'ok'

    message_dict = Feedback_message.message_dict
    frame = cv2.putText(frame, message_dict[key]['text'], (100,100),
        cv2.FONT_HERSHEY_SIMPLEX, 1.0, message_dict[key]['color'], 2)

    return frame

def pass_to_server(ip, port, frame):
    if ip[-1] != ':':
        ip += ':'
    print('request to server({})'.format(ip+port))

    with grpc.insecure_channel(ip+port) as channel:
        stub = proto_sample_pb2_grpc.AI_OnlineMonitoringServiceStub(channel)

        result = stub.process(
            proto_sample_pb2.UserRequest(
                img_bytes = bytes(frame),
                width = frame.shape[1],
                height = frame.shape[0],
                channel = frame.shape[2]
            )
        )
    return result


def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='localhost:',
        help='server ip address. (default:localhost:)')
    parser.add_argument('--port', type=str, default='16011', help='server port. (defult:15011)')
    return parser.parse_args()

def main():

    args = opt()

    # webcam object
    webcam = cv2.VideoCapture(0) # camera index
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        _, frame = webcam.read()

        result = pass_to_server(args.ip, args.port, frame)
        frame = distance_based_feedback(result.distance, frame)

        cv2.imshow('window', frame)
        key = cv2.waitKey(330) 
        
        if key == ord('q'): # ascii
            break

if __name__ == '__main__':
    main()
