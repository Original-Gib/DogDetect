#!/bin/bash

pulseaudio --start #start the pulseaudio sound server
bluetoothctl power on #Power on bluetooth  
bluetoothctl connect 04:52:C7:C6:A8:54 #connect to mac address of audio device via bluetooth