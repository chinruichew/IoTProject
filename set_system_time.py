import os
from datetime import datetime
from mqtt_client import *
import config as config

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    time_now = datetime.now()
    year_now = time_now.year
    time_gps = datetime.strptime(payload, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)
    year_gps = time_gps.year

    print('year_gps: ', year_gps)
    print('time_gps: ', str(time_gps))
    if (year_gps == year_now):
	return

    #if (year_gps >= 2018):
	#os.system('sudo date --set \"' + str(time_gps) + '\"')

if __name__ == "__main__":
    #initializing MQTT client, connection and subscription
    pid = str(os.getpid())
    connect_to_local_broker(config.system_time_client_name + '-' + pid)
    subscribe(config.gps_time_topic)
    set_on_message(on_message)
    receive_data()
