#!/usr/bin/env bash

python /home/pi/phatmeter/server.py > /dev/null 2>&1 &
python /home/pi/phatmeter/mqtt.py > /dev/null 2>&1 &

running=true

echo "Press control-c to quit!"

trap ctrl_c INT

function ctrl_c() {
    killall python
    running=false
}

while $running
do
    sleep 1
done
