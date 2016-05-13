# Raspberry Installation
apt-get install mosquitto
apt-get install mosquitto-clients

# Mosquitto Tool for Windows
http://mqttfx.jfx4ee.org/

Subscribing to a topic on raspberry
```sh
$ mosquitto_sub -h 192.168.3.14 -t test
```
Publish messages to a topic on raspberry
```sh
$ mosquitto_pub -h 192.168.3.14 -t test -m "Testing this stuff" 
```

## Phyton library for Raspberry
https://pypi.python.org/pypi/paho-mqtt/1.1

## Example Script for receiving messages and turn on LED
```phyton
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.payload == 'ON':
	GPIO.output(18, True)

    if msg.payload == 'OFF':
	GPIO.output(18, False)

    print(msg.topic+" "+str(msg.payload))
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```