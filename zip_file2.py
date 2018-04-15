import os
import time
import config as config
from datetime import datetime

def zip_file():
    dirs = os.listdir(config.data_dir)
    time_now = datetime.now().replace(second=0, microsecond=0)

    for dir in dirs:
        time_dir = datetime.strptime(dir, '%Y%m%d%H%M%S')
        if (time_now > time_dir):
            # zipped_path = config.zipped_dir + dir + '.gz'
            zipped_path = config.zipped_dir + dir + '.zip'
            print(zipped_path)
            data_path = config.data_dir + dir
            print(data_path)
            # zip -r compressed_filename.zip foldername
            cd_command = 'cd ' + data_path + '/'
            os.chdir(data_path + '/')
            zip_command = 'sudo zip -r ' + zipped_path + ' ./*'
            os.system(zip_command)
            print(cd_command)
            print(zip_command)
            # os.system('sudo tar -czf ' + zipped_path + ' ' +  data_path)
            # os.system('sudo rm -r ' + data_path)

if __name__ == "__main__":
    zip_file()