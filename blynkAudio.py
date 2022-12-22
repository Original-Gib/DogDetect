#!/usr/bin/python3

import BlynkLib
from subprocess import call

#Function to call the btconnect script to connect to the bluetooth device when the blynkAudio script is run
call(["sh", './btconnect.sh'])

BLYNK_AUTH = 'UOWznNZRG8aCkAD25IGa3xcZqoow4zBi'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#datastream for the blynk app
#Linked to button on the Blynk mobile app 
#When button is pressed the playAudio script is run to play the whistle wav file from the audio folder
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Whistle playing')
    if buttonValue=="1":
        call(["sh", './playAudio.sh'])
    else:
        print('Button Relased')

while True:

    blynk.run()