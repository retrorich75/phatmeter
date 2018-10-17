# Enviro pHAT Meter web/MQTT server 

## Getting Started
If your new to Raspberry Pi world start here https://www.raspberrypi.org/documentation/setup/
and for connectivity here https://www.raspberrypi.org/documentation/configuration/wireless/README.md
* NB if your using a RPI Zero/A+/2/3 without the built-in wifi don't forget you'll need an USB Wifi dongle.

### Requirements
* Raspberry Pi Zero/ZeroW/A+/2/3/3+ (https://www.raspberrypi.org/products/)
* NOOBS/Raspbian 4.9 on micro/SD Card (https://www.raspberrypi.org/downloads/)
* Pimoroni Enviro pHat https://shop.pimoroni.com/products/enviro-phat

### Installing
* Environ pHAT libraries, instructions can be found [here](https://github.com/pimoroni/enviro-phat)
* Flask http://flask.pocoo.org/ (web server)
```
pip install flask
```
This is what you should see in the terminal
![Finding the terminal](https://github.com/retrorich75/commonfiles/blob/master/pip_install_flask.png?raw=true)
* Clone this repo, command to type in a Terminal
```
git clone https://github.com/retrorich75/phatmeter.git
```
You should see something similar to the below
![Finding the terminal](https://github.com/retrorich75/commonfiles/blob/master/git-clone-phatmeter.png?raw=true)

### The servers
* Flask (web server) - http://flask.pocoo.org/
* MQTT (machine-to-machine (M2M)/"Internet of Things" server - http://mqtt.org/

### Usage
* Flask : show the details of the Enviro pHAT in a web browser.
Run in a terminal on your Pi the following commands
```
cd phatmeter
```
then type "./server.py"
```
./server.py
```
You should see the below output
![Finding the terminal](https://github.com/retrorich75/commonfiles/blob/master/flask_server-running.png?raw=true)

* Now open a web browser on the host name or IP address of your Pi with the port 5000
You should see something similar to the below
![Finding the terminal](https://github.com/retrorich75/commonfiles/blob/master/flash-web-envirophat.png?raw=true)

* MQTT : share Enviro pHAT measurements for further use.
TBD

## Versioning
* version 1.1

## Authors
* **Lars Juhl Jensen** - *Initial work* - https://github.com/larsjuhljensen/phatmeter/ 
* **Richard M Parslow** - updated code and documentation https://github.com/retrorich75/phatmeter/
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Raspberry Pi Foundation https://www.raspberrypi.org/about/ for their devices 
* Pimoroni https://shop.pimoroni.com/ (Pirate, Monkey, Robot, Ninja (Pi-Mo-Ro-Ni)) pirates aka Jon Williamson and Paul Beech for their continued developement of hardware for the Raspbery Pi and other tech devices.
