import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="hw3_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="JDS/WEBCAMS/JETSONTX2"

REMOTE_MQTT_TOPIC="JDS/WEBCAMS"
REMOTE_MQTT_PORT=1883
REMOTE_MQTT_HOST="130.198.99.9"



def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote   
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 360)               
remote_mqttclient.loop_start()


def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received!")	
    msgcontent = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, msgcontent, 1)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient=mqtt.Client()                                                  
local_mqttclient.on_connect = on_connect_local   
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)                  
local_mqttclient.on_message = on_message  

local_mqttclient.loop_forever()    
remote_mqttclient.loop_stop()
