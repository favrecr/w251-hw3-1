# w251-hw3 - Homework 3  
  
## Overview
Thhis repo contains the components of a lightweight IoT application pipeline that collects images of faces detected from a webcam feed on an edge device (the Nvidia Jetson TX2) and transmits them to the cloud to be processed and stored (aIBM CLoud Object Store).   
  
## Implementation Details  
All components are implemented as containerized applications deployed on the edge device (to capture and forward image) and the cloud (to receive, process and store). MQTT proticik us ysed for communication and transmitting images across components.  

### Overall Architecture  

  
### Jetson TX2 
  


### IBM CLoud  

Mounted an IBM Objectstore bucket to the `/HW3Images` directory  

### Docker  
Build Images for the Cloud:  
Broker: `docker build -t hw3_broker -f Dockerfile.broker .`  
Image Processor: `docker build -t hw3_processor -f Dockerfile.processor .`  
  
Build Images for the Jetson  
Broker: `docker build -t hw3_broker -f Dockerfile.broker .`  
Forwarder: `docker build -t hw3_forwarder -f Dockerfile.forwarder .`  
Edge Image Detector: `docker build -t hw3_edge -f Dockerfile.processor .`  
  
## MQTT messgaing with Mosquitto  

  

### Python Scripts  

## Execution Instructions  

### In the CLoud VSI:  
Create a user-defined Docker network: `docker network create --driver bridge hw03_jds`  
Initiate the cloud MQTT Broker: `docker run --name hw3_broker --privileged -tid --rm -p 1883:1883 --network hw03_jds hw3_broker`  
Initiate the Image Processor: `docker run --name hw3_processor -v /HW3Images:/HW3Images -v /home/Projects/w251-hw3:/host --privileged -ti --rm --network hw03_jds hw3_processor python /host/imageprocess.py`  
  
### On the Jetson TX2:  
Create a user-defined Docker network: `docker network create --driver bridge hw03_jds`  
Initiate the local MQTT Broker: `docker run --name hw3_broker --privileged -tid --rm -p 1883:1883 --network hw03_jds hw3_broker`  
Launch the Edge Detecor: `docker run --name hw3_edge -e DISPLAY=$DISPLAY --privileged -v /usr/share/opencv4:/OpenCV -v /tmp:/tmp -v /home/nvidia/Documents/Projects/HW3:/host --rm --env QT_X11_NO_MITSHM=1 -ti --network hw03_jds hw3_edge python /host/edge_detect.py`  
Launch the Forwarder: `docker run --name hw3_forwarder -v /home/nvidia/Documents/Projects/w251-hw3:/host --privileged -ti --rm --network hw03_jds hw3_forwarder python3 /host/forward.py`  
  
The usb webcam for the TX2 should now start capturing faces and sending it to the cloud where it gets stored in the COS bucket mounted at /HW3Images  
  
## Sample Images    
  
Captured images (in COS Bucket: jds-w251-hw3-images):   https://s3.au-syd.cloud-object-storage.appdomain.cloud/jds-w251-hw3-images  
  
Some sample images also included:    
![alt text](image414.png)
![alt text](image44.png)
![alt text](image7.png)
![alt text](image187.png)
![alt text](image180.png)
![alt text](image109.png)


## Conclusion
While this project does have a working End to End flow for image detection at teh edge, with transmission to and storage on the cloud... a few things that could be worked on (given more time) to improve the seamlessness of the implementation:  
1. Use docker-compose to make set up/ teardown (both on the cloud VSI and the Jetson) simpler (i.e. less steps)  
2. Have a more graceful way to stop image capture , transmission and storage. This could be accomplished by using a time limit or a "shutdown" topic that the Edge Detector , Forwarder and Processor subscribe to.  
3. Live feedback of faces being captured (in debug mode) on the Jeston (would require external monitor to be attached) with rectangles on the faces being captured overlayed in the video feed.  




