# AI Online Monitoring Service

![my_figure](test.png)

Inspired by....
This project tracks the face of a user using the webcam to warn them if their eyes wander or if they are too close to the screen. 

## 1. Installation

### 1.1. Anaconda Environment

I highly recommend using the provided yaml to initialize the environment.

```bash
conda env create -f AIMonitoringServiceEnvZIP.yaml
```

(optional) You can also create your own environment by following this command.
```bash
conda create -n <ENV_NAME> python=3.8
```

Dependencies can be found in the file **requirements.txt** in this repo.

### 1.2. gRPC build

You can use this to create a one-time setup for gRPC proto.

```bash
bash build_grpc_pb.sh
```

### 1.3 FaceBoxes build

In my implementation, I used BSD Faceboxes, found at this link:

[FaceBoxes](https://github.com/zisianw/FaceBoxes.PyTorch)

You can use this to create a one-time setup for FaceBoxes.

```bash
cd FaceBoxes
bash build_cpu_nms.sh
cd ..
```

## 2. How to Run

### 2.1. Server Side
To run the server side, follow this command:

```
python server.py --port <PORT_NUM>
```

### 2.2. Client Side

To run the client side, follow this command:

```
python client.py --ip <IP_ADDRESS> --port <PORT_NUM>
```

