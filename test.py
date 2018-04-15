import paho.mqtt.client as mqtt
import datetime
import time
import gzip

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('samba/a/b/c/iow/sensor')

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(str(msg.payload))
    current_time = time.time()
    """
    with gzip.open(str(current_time) + '.gz', 'wb') as f:
        print("File written!")
        f.write(msg.payload)
    """
    with open(str(current_time) + '.csv', 'w') as f:
        f.write(msg.payload)
        print("File written!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('13.228.43.162', 1883, 60)
# client.connect('localhost')

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()