import paho.mqtt.client as mqtt
import os, urlparse
import time

mqttc = mqtt.Client()
topic = 'test'

# Connect
mqttc.username_pw_set("wqbleknw", "bxG3QCxArnWt")
mqttc.connect("farmer.cloudmqtt.com", "11860")

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
while(1):
	mqttc.publish(topic, "hi!")
	time.sleep(1)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
