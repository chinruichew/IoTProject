import os
import config as config

def count_file():
    dirs = os.listdir(config.data_dir)
    no_of_files = ''

    for dir in dirs:
	data_path = config.data_dir + dir
	cnt = os.popen('sudo ls ' + data_path  + ' | wc -l').read()
	no_of_files += ','.join([dir, cnt])

    return no_of_files

def save_to_file(data):
    with open(config.test_accel_frequency_result, 'a') as fd:
	fd.write(data)

if __name__ == "__main__":
    data = count_file()
    save_to_file(data)
