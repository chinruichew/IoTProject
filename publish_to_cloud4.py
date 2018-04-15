import os
import time
from mqtt_client import *
import config as config
from datetime import datetime
import urllib

def publish_data_at_x_frequency(time_block):
    archive = '/home/pi/internet_of_wheels/mqtt_test/archive/'
    while True:
        try:
            url = "https://www.google.com"
            urllib.urlopen(url)
            status = "Connected"
        except:
            status = "Not connected"
        print status
    
        if status == "Connected":
            print("running")
            start_time = time.time()
            
            time_now = datetime.now()
            dir_name = time_now.replace(microsecond=0).strftime('%Y%m%d%H%M%S')
            current_file = config.data_dir + dir_name + '.csv'
            
            dir = os.listdir(config.data_dir)
            for file_name in dir:
                if file_name != current_file:
                    file_path = config.data_dir + file_name
                    with open(file_path, 'r') as f:
                        data = f.read()
                        publish(config.project_topic, data)
                    #print(data)
                    print(file_name)
                    print(current_file)
                    print("file written!")
                    #os.system('sudo rm -r ' + file_path)
                    os.system('sudo mv ' + file_path + ' ' + archive)
                    #time.sleep(2)
            
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