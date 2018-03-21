# Samba_IOT

##Finding out IP Address of Raspberry Pi to connect to

##Ensure that IPV6 on Ethernet Controller is diabled

###(First Time Configuration)
1. Configure Static IP address to 1.1.1.0
2. Subnet Mask to 255.255.255.0
3. Login through Putty 1.1.1.1 (Username:Pi, Password:iot5%)

###Setting up wifi connections
1. In the same connection, sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
2. Under the network with the highest priority, adjust your SSID & PSK accordingly
3. Restart PI Device
4. Reconnect to 1.1.1.1 and type iwconfig (If ESSID is not blank, means it is successfully connection)
5. Type the command ifconfig to get your PI IP Address in your putty terminal
6. Under wlan0, your Inet address will display your IP address
7. Under those configuration, you then proceed to connect to the IP address with putty

##After setting up, if forgotten IP address, just repeat Setting up wifi connections (Steps 4 - 7)

##Tips

1. To check commands (ps -ef | grep collect)
2. sudo date -s {date}

##Auto generated folders when running run.sh
1. data
2. tmp
3. logs
4. zipped_Data
