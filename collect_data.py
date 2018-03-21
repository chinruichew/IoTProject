import os
from datetime import datetime
from mqtt_client import *
import config as config

gps_data = ''

def on_message(client, userdata, message):
    global gps_data

    time_now = datetime.now()
    dir_name = time_now.replace(second=0, microsecond=0).strftime('%Y%m%d%H%M%S')
    dir_path = config.data_dir + dir_name + '/'
   
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    print(dir_path)

    topics = str(message.topic)
    payload = str(message.payload.decode("utf-8"))

    topic_lists = topics.split('/')

    if ((topic_lists[0] == 'gps') and (topic_lists[1] == 'data')):
       gps_data = payload
       return

    if (topic_lists[0] == 'accelerometer'):
        accel_data = payload

    data = ','.join([accel_data, gps_data])
    #print(data)
    file_name = str(time_now)

    with open(dir_path + file_name, 'a') as fd:
        fd.write(data)

if __name__ == "__main__":
    #initializing MQTT client, connection and subscription
    pid = str(os.getpid())
    connect_to_local_broker(config.write_data_client_name + '-' + pid)

    subscribe(config.gps_topic)
    subscribe(config.accel_topic)

    set_on_message(on_message)

    receive_data()
