# w251-hw3 - Homework 3

## Overview
Thhis repo contains the components of a lightweight IoT application pipeline that collects images of faces detected from a webcam feed on an edge device (the Nvidia Jetson TX2) and transmits them to the cloud to be processed and stored (aIBM CLoud Object Store).

## Implementation Details
All components are implemented as containerized applications deployed on the edge device (to capture and forward image) and the cloud (to receive, process and store). MQTT proticik us ysed for communication and transmitting images across components.

### Overall Architecture


### Jetson TX2 



### IBM CLoud


### Docker
Build Images for the Cloud:
Broker: `docker build -t hw3_broker -f Dockerfile.broker .`
Image Processor: `docker build -t hw3_processor -f Dockerfile.processor .`

Build Images for the Jetson
Broker: `docker build -t hw3_broker -f Dockerfile.broker .`
Forwarder: `docker build -t hw3_forwarder -f Dockerfile.forwarder .`
Edge Image Detector: 

## MQTT messgaing with Mosquitto



### Python Scripts

## Execution Instructions

docker run --name hw3_broker --privileged -tid --rm -p 1883:1883 --network hw03_jds hw3_broker

docker run --name hw3_processor -v /HW3Images:/HW3Images -v /home/Projects/w251-hw3:/host --privileged -ti --rm --network hw03_jds hw3_processor python /host/imageprocess.py




## Sample Images


## Conclusion





