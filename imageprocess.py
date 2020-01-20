import numpy as np
import cv2
import paho.mqtt.client as mqtt

#Set up MQTT parameters
LOCAL_MQTT_HOST="hw3_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="JDS/WEBCAMS"

#Path to store images
OUTPUT_STR="/HW3Images/image"

#Ensure Subscribe on connect
def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC,1) 

index=0
#Process incoming messages
def on_message(client,userdata, msg):                                        
        global index 
  	try:                                                                       
    		print("message received!")                                               
    		index=index+1
                msgcontent = msg.payload                                                        
                frame=np.frombuffer(msgcontent,np.int8)
                img=cv2.imdecode(frame,1)
                cv2.imwrite(OUTPUT_STR+str(index)+".png",img)
        except:
    	        print("Unexpected error:", sys.exc_info()[0])



#Instantiate MQTT client
local_mqttclient=mqtt.Client()
local_mqttclient.on_connect = on_connect_local 
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 360)               
local_mqttclient.on_message = on_message


local_mqttclient.loop_forever()
 
