import paho.mqtt.client as mqtt

def connect_to_local_broker(client_name):
    global client
    client = mqtt.Client(client_name)
    client.connect("localhost")
    print('connect to local broker')

def connect_to_external_broker(client_name, broker):
    global client
    client = mqtt.Client(client_name)
    client.tls_set(certfile="./smartbfa_srv.crt",
               ca_certs="./smartbfa_ca.crt",
               keyfile="./smartbfa_srv.key")
    #client.connect(broker)
    client.connect("smartbfa.com", 8883)

def publish(topic, data):
    client.publish(topic, data) 

def subscribe(topic):
    client.subscribe(topic, 0)
    print('subsribe')

def set_on_message(on_message):
    client.on_message = on_message
    print('set on message')

def receive_data():
    print('receive data')
    client.loop_forever()
    print('end loop start')
