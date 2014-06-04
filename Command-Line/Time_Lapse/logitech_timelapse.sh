#!/bin/sh
# Time lapse capture using fswebcam
# Takes a snapshot every $INTERVAL seconds
# Saves into current directory


INTERVAL=5
CONFIG_FILE="logitech_fswebcam_config.conf"

while true; do
	fswebcam --config $CONFIG_FILE --save ./$(date +%Y-%m-%d-%H-%M-%S).jpg
	sleep $INTERVAL
done
