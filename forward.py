import numpy as np
import cv2
import paho.mqtt.client as mqtt

#Setup MQTT Information
LOCAL_MQTT_HOST="hw3_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="JDS/WEBCAMS/JETSONTX2"



#Instantiate MQTT Client and connect to Broker

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

local_mqttclient=mqtt.Client()
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 30)
local_mqttclient.loop_start()


# Start capturing bode from usb webcam (Device 1)
cap=cv2.VideoCapture(1)

#i=0   #Initialize counter for face images

while(True):

    ret,frame=cap.read()  #Read Frame

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #Convert to Gray Scale
    
    face_cascade=cv2.CascadeClassifier('/OpenCV/haarcascades/haarcascade_frontalface_default.xml')   #Run Face classification

    faces=face_cascade.detectMultiScale(gray,1.3,5)
    if len(faces)>0: print(faces)
    
    
    #For each face detected in frame, captureimage and publish to local MQTT broker

    for (x,y,w,h) in faces:
        
        face=gray[y:y+h,x:x+w]   #Cut out the face
        
        #print("face = ",face)
        #cv2.imwrite('/host/image'+str(i)+'.png',face) 

        rc,png =cv2.imencode('.png',face)  #Encode as png

        msg=png.tobytes()  #Prep to send as message

        local_mqttclient.publish(LOCAL_MQTT_TOPIC,msg,1)  #Publish to local broker
        #i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

local_mqttclient.loop_stop()

local_mqttclient.disconnect()
cap.release()
cv2.destroyAllWindows()
