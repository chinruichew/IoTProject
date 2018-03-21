import os
import time
from adxl345 import ADXL345
from mqtt_client import *
import config as config
import datetime

def read_accel_data(adxl345):
    try:
        axes = adxl345.getAxes(True)
	time = unicode(datetime.datetime.now())
        accel_data = ','.join([time, str(axes['x']), str(axes['y']), str(axes['z'])])

        return accel_data
    except Exception as e:
        print('Error reading accelerometer data')
        return

def publish_data_at_x_frequency(adxl345, time_block):
    while True: 
        start_time = time.time()
        accel_data = read_accel_data(adxl345)
        publish(config.accel_topic, accel_data)
        print(accel_data)
        delay = time_block - (time.time() - start_time)
        if (delay > 0): #delay can be negative
            time.sleep(delay)

if __name__ == "__main__":
    #initializing MQTT client and connection
    pid = str(os.getpid())
    connect_to_local_broker(config.accel_client_name + '-' + pid)

    adxl345 = ADXL345()
    time_block = float(1)/float(config.accel_frequency)
    
    publish_data_at_x_frequency(adxl345, time_block)

