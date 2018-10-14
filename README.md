# Enviro pHAT Meter web/MQTT server 

Requirements:
Raspberry Pi Zero/ZeroW/2/3/3+ (https://www.raspberrypi.org/products/)
NOOBS/Raspbian OS on micro/SD Card (https://www.raspberrypi.org/downloads/)

If your new to Raspberry Pi world start here https://www.raspberrypi.org/documentation/setup/
and for connectivity here https://www.raspberrypi.org/documentation/configuration/wireless/README.md
NB if your using a RPI Zero/2/3 without the built-in wifi don't forget you'll need a USB Wifi dongle.

Pimoroni Enviro pHat https://shop.pimoroni.com/products/enviro-phat

The servers:
Flask (web server)
MQTT (machine-to-machine (M2M)/"Internet of Things" server 

Usage:
Flask : show the details of the Enviro pHAT in a web browser.
MQTT : share Enviro pHAT measurements for further use.

This fork is based on https://github.com/larsjuhljensen/phatmeter by Lars Juhl Jensen
