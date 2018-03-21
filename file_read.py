import os
import time
from datetime import datetime

"""
def zip_file():
    while True:
        dirs = os.listdir(config.data_dir)
        time_now = datetime.now().replace(second=0, microsecond=0)

        for dir in dirs:
	    time_dir = datetime.strptime(dir, '%Y%m%d%H%M%S')
	    if (time_now > time_dir):
		zipped_path = config.zipped_dir + dir + '.gz'
		data_path = config.data_dir +  dir
	        os.system('sudo tar -czf ' + zipped_path + ' ' +  data_path)
	        os.system('sudo rm -r ' + data_path)

if __name__ == "__main__":
    zip_file()
"""

path = "C:/Users/nubcaked/Desktop/internet_of_wheels_workspace/mqtt_test/zipped_data/"

# print(os.listdir(path)[0])
file = os.listdir("C:/Users/nubcaked/Desktop/internet_of_wheels_workspace/mqtt_test/zipped_data")[0]

f = open(path + file, 'rb')
print(f.read())