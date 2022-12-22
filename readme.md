***************************************************

DogDetect - IOT Application

***************************************************

Video Link: https://www.youtube.com/watch?v=h9k3mYl6dQU


---------------------------------------------------
                   Features
---------------------------------------------------
1) Use motion detector to monitor your pets area and alert you to movement in the area

2) If motion is detected email is sent to your email address

3) If no motion is detected for some time you will receive a notification from your Blynk app to alert you that
   no movement has been detected

4) Access a livestream video of the area to tune into what your pet is up to

5) Connect a wireless speaker to your DogDetect device and use your Blynk app to play a whistle noise to attract the
   attention of your pet 


---------------------------------------------------
                   Configuration
---------------------------------------------------

*************
Bluetooth
*************

1) Install Pulse audio by running 'sudo apt-get install pulseaudio*'
2) Add pi user to lp group by running 'sudo usermod -a -G lp pi'
3) Reboot your device by running 'sudo reboot'
4) Start pulse audio by running 'pulseaudio --start'
5) Access bluetooth by running 'sudo bluetoothctl'
6) Power on the bluetooth with the command 'power on'
7) Select default agent with the command 'default-agent'
8) Turn on your bluetooth device and put it in pairing mode
9) Start a bluetooth scan by running 'scan on'
10) Locate your bluetooth device and then add it to the trusted devices with the command 'trust xx:xx:xx:xx'
11) Pair to the bluetooth device with 'pair xx:xx:xx:xx'
12) Connect with your bluetooth device with 'connect xx:xx:xx:xx'
13) Exit pulse audio by running 'exit'
14) Find your device in your devices list by running 'pactl list cards short' and note the device number
15) Update the device number in the playAudio.sh file


*************
Blynk
*************

1) Set up device on Blynk
2) Add Blynk auth token to the api.py file and the blynkAudio.py file
3) Create events in Blynk
    3.1) Event Name: Movement detected. Configure to sent to timeline
    3.2) Event Name: hour since last movement. Configure to send notification to user device
4) Add video stream module and set URL to http://[IP Address]:8000/stream.mjpg
5) Create datastream on virtual pin 0, min: 0, max: 0, default: 0
6) Add button module, set to the created datastream, on: 1, off: 0, mode PUSH


*************
SMTP
*************

1) Add your SMTP details to the send_mail function in api.py file
2) Edit send mail function on line 66 of api.py to send to your email address


---------------------------------------------------
                   Running
---------------------------------------------------

1) Run the discoServer.py file from the discovery folder
2) Run blynkAudio.py file
3) In a separate window run api.py
4) Run assignment.py file from SBC in the PacketTracer file 
5) Simulate motion by pressing ALT and moving curser in front of the motion sensor


---------------------------------------------------
                   Bugs
---------------------------------------------------

1) Unable to run both the api.py file as well as the cameraStream.py file due to the use of camera resources


---------------------------------------------------
                   Resources used
---------------------------------------------------

1) https://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming
2) https://wiretuts.com/connecting-bluetooth-audio-device-to-raspberry-pi
3) https://docs.blynk.io/en/getting-started/events-tutorial
4) https://tutorial.cytron.io/2021/03/16/blynk-video-streaming-using-raspberry-pi-camera/
