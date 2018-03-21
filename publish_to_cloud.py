import os
import time
from mqtt_client import *
import config as config
import datetime
from hashlib import md5
import pickle

def publish_data_at_x_frequency(time_block):
    m = md5()
    while True: 
        start_time = time.time()
        
        dir = os.listdir(config.zipped_dir)
        for file_name in dir:
            file_path = config.zipped_dir + file_name
            with open(file_path, 'rb') as f:
                byte_array = bytearray(f.read())
                m.update(byte_array)
                file_hash = m.hexdigest()
                payload_json = {'byte_array': byte_array, 'md5': file_hash}
                # print(f.read())
                # print(file_bytes)
                # publish(config.project_topic, file_bytes)
                publish(config.project_topic, pickle.dumps(payload_json))
            #print(data)
            os.system('sudo rm -r ' + file_path)
            time.sleep(2)
        
        delay = time_block - (time.time() - start_time)
        
        if (delay > 0): #delay can be negative
            time.sleep(delay)
            
if __name__ == "__main__":
    #initializing MQTT client and connection
    pid = str(os.getpid())
    #connect_to_local_broker(config.accel_client_name + '-' + pid)
    connect_to_external_broker(config.main_client_name + '-' + pid, config.broker_ip)

    time_block = config.publish_interval
    
    publish_data_at_x_frequency(time_block)