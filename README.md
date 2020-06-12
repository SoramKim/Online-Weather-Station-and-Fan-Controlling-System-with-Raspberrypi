## OSS Final Project 
---------------------------
# Online Weather Station and Fan Controlling System
## 기능
* 온도와 습도를 1초마다 측정한다 
* 온도가 특정 값 이상으로 넘어가면 빨간 LED ON, Cooling Fan 작동
* 습도가 특정 값 이상으로 넘어가면 초록 LED ON, Cooling Fan 작동
* 온도와 습도 값을 OLED에 display 해준다

* 온도값을 1분마다 crontab을 이용해 자동으로 측정해 web server를 통해 현재 온도를 확인할 수 있다. 

## 준비물
* 라즈베리파이
* DHT11 온습도 센서
* SSD1306 OLED
* Red and Green LED
* 220옴 저항 2개
* Cooling Fan (냉각팬)
* 점퍼선(M/F) 과 Bread Board

# 주요 파일 설명
weatherStation.py : 온습도에 따라 cooling fan과 led를 제어하고 OLED에 측정 값을 diaplay해주는 파이썬 코드이다. while문을 돌며 계속 실행, ctrl+C 를 누르면 종료 

weatherStation_cron.py : 웹 서버 상에서 온도를 확인 하기 위한 코드로 온습도가 한번만 측정 된다. crontab을 이용하여 이 코드가 1분마다 측정된다.

cron_temp.sh : weatherStation_cron.py을 실행하기 위한 shell script이다. crontab에서 1분마다 자동으로 이 shell script가 실행되어 weatherStation_cron.py를 통해 온습도를 측정한다.

onlineWeatherStation.php : 웹 서버 상에서 weather station에 들어갔을 때 온습도를 확인 할 수 있게 하는 php 파일이다.

# Why is this project useful?
* 온습도에 따라 자동으로 Cooling fan을 제어
* 온습도에 따른 led 표시기능 및 OLED를 통한 현재 온도 Display
* Online server를 통해 현재 온도 및 습도 확인 가능

# How do I get started?
*   RPI.GPIO 설치 
<pre>
<code>
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install RPi.GPIO
</code>
</pre>

* Python Imaging Library 설치
<pre>
<code>
sudo apt-get install python-imaging python-smbus
</code>
</pre>

* OLED (SSD1306) Python Library 설치
<pre>
<code>
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
</code>
</pre>

* 온습도 센서 데이터 획득을 위한 Adafruit_DHT Library 설치
<pre>
<code>
sudo pip3 install Adafruit_DHT
</code>
</pre>

# Where can I get more help, if I need it?
<https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage>
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/9
http://raspberrypi4u.blogspot.com/2017/03/raspberry-pi-dht-sensor-oled.html
https://www.letmecompile.com/scheduler-cron-tutorial/

# License 
Online Weather Station and Fan Controlling System 

Written by Soram Kim(soram523@gmail.com). 
MIT license, all text above must be included in any redistribution

