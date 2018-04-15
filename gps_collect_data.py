import os
import time
from datetime import datetime, timedelta
from dateutil import tz
from gps import *
from mqtt_client import *
import config as config

def read_gps_data(gpsd):
    try:
        mode = gpsd.fix.mode

        latitude = gpsd.fix.latitude
        epy = gpsd.fix.epy

        longitude = gpsd.fix.longitude
        epx = gpsd.fix.epx

        altitude = gpsd.fix.altitude
        epv = gpsd.fix.epv

        speed = gpsd.fix.speed
        eps = gpsd.fix.eps

        climb = gpsd.fix.climb
        epc = gpsd.fix.epc

        track = gpsd.fix.track
        epd = gpsd.fix.epd

        numSatellites = 0
	#print('satellites', gpsd.satellites)
        for i in gpsd.satellites:
	    # check why must end with y 
            if str(i).endswith('y') == True:
                numSatellites += 1

        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
	gps_utc_time = datetime.strptime(gpsd.utc, '%Y-%m-%dT%H:%M:%S.%fZ')
        gps_utc_time = gps_utc_time.replace(tzinfo=from_zone)
        gps_local_time = gps_utc_time.astimezone(to_zone).replace(tzinfo=None)

    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print ("\nKilling Thread...")
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
        print ("Done.\nExiting.")
    except (Exception, e):
        print ('Error handling GPS Receiver with exception e {}.'.format(e))

    gps_data = ','.join([str(mode), str(latitude), str(epy), str(longitude), str(epx), str(climb), str(epc), str(altitude), str(epv), str(speed), str(eps), str(track), str(epd), str(numSatellites)])

    return (gps_data, str(gps_local_time))

def publish_gps_data_at_x_frequency(gpsd, time_block):
    while True:
        if gpsd != None: #this will continue to loop and grab each set of gpsd info to clear the buffer
            start_time = time.time()
            gpsd.next() #activate if gps signal is available
            try:
                (gps_data, gps_time) = read_gps_data(gpsd)
                publish(config.gps_topic, gps_data)
                publish(config.gps_time_topic, gps_time)

                print(gps_data)
                delay = time_block - (time.time() - start_time)
                if (delay > 0):
                    time.sleep(delay)
            except Exception as e:
                print ('Error publishing GPS sensor with exception {}'.format(e))

if __name__ == "__main__":
    os.system('sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock') #ensuring gpsd is pointed to the right USB GPS receiver
    #os.system('sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock') #ensuring gpsd is pointed to the right USB GPS receiver
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info

    #initializing MQTT client and connection
    pid = str(os.getpid())
    connect_to_local_broker(config.gps_client_name + '-' + pid)
    time_block = float(1)/float(config.gps_frequency)
    publish_gps_data_at_x_frequency(gpsd, time_block)
