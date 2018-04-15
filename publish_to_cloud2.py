import os
import time
from mqtt_client import *
import config as config
import datetime

def publish_data_at_x_frequency(time_block):
    while True: 
        start_time = time.time()
        
        dir = os.listdir(config.data_dir)
        for file_name in dir:
            file_path = config.data_dir + file_name
            with open(file_path, 'rb') as f:
                data = bytearray(f.read())
                publish(config.project_topic, data)
            #print(data)
            print("file written!")
            os.system('sudo rm -r ' + file_path)
            time.sleep(2)
        
        delay = time_block - (time.time() - start_time)
        
        if (delay > 0): #delay can be negative
            time.sleep(delay)
            
if __name__ == "__main__":
    #initializing MQTT client and connection
    pid = str(os.getpid())
    #connect_to_local_broker(config.main_client_name + '-' + pid)
    connect_to_external_broker(config.main_client_name + '-' + pid, config.broker_ip)

    time_block = config.publish_interval
    
    publish_data_at_x_frequency(time_block)
    
#with ZipFile('spam.zip', 'w') as myzip:
#    myzip.write('eggs.txt')