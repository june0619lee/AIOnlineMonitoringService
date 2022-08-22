import grpc
import proto_sample_pb2, proto_sample_pb2_grpc

import os
import cv2 # webcam control; image processing
import argparse

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='localhost:', help='server ip address. (default:localhost:)')
    parser.add_argument('--port', type=str, default='15011', help='server port. (defult:15011)')

    return parser.parse_args()

def main():

    args = opt()

    # webcam object
    webcam = cv2.VideoCapture(0) # camera index
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while True:
        _, frame = webcam.read()

        # print(type(frame)) # np.ndarray
        # print(frame.shape)

        cv2.imshow('window', frame)
        key = cv2.waitKey(33) # 33 milliseconds / frame
                              # => frame per second (fps)
                              # 30 frames = around 1 second processing

        if key == ord('q'): # ascii
            break
        elif key == ord('s'):
            cv2.imwrite('./test.png', frame)
            break

if __name__ == '__main__':
    main()