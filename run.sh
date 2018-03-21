#!/bin/bash

# Run accelerometer data collection script
nohup python accel_collect_data.py > logs/accel_log &

# Run GPS data collection script
nohup python gps_collect_data.py > logs/gps_log &

# Run set system time script 
nohup python set_system_time.py > logs/system_time_log &

# Run data writing script
nohup python collect_data.py > logs/collect_log &

# Run zip file script
nohup python zip_file.py > logs/zip_log &


