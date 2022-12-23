#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_cors import CORS
from picamera import PiCamera
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import BlynkLib
from time import sleep


BLYNK_AUTH = '' #enter you Blynk app auth token
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

deviceID="device1"
#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

# Function to send an email and attachment using SMTP
def send_mail(eFrom, to, subject, text, attachment):
    # SMTP Server details
    smtpServer='' #enter you smtp server
    smtpUser='' #enter your smtp username
    smtpPassword='' #enter your smtp password
    port=587

    # open attachment and read in as MIME image
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msgImage['Content-Disposition'] = 'attachment; filename="image.jpg"'
    msg.attach(msgImage)
    msg['Subject'] = subject

    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()

#API Functions

#Route to call the capture function:
#This function will trigger the PI camera to capture an image and call the send_mail function to send this image 
#to the the users email address. 
#The function will also trigger a Blynk event to log on the Blynk app timeline when movement has been detected
@app.route('/dogdetect/capture',methods=['POST'])
def capture():
    camera = PiCamera()
    camera.start_preview()
    currentTime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    fileLoc = f'/home/pi/assignment/images/motion@{currentTime}.jpg' # set location of image file and current time
    camera.rotation = 180
    camera.capture(fileLoc) # capture image and store in fileLoc
    print(f'Image taken at {currentTime}') # print frame number to console
    camera.close()
    text= f'Hi,\nMotion detected at {currentTime}'
    send_mail('activity@dogdetect.ie', 'adamhenrygibson@gmail.com', 'Motion Detected',text, fileLoc)# Send the email 
    blynk.log_event("movement_detected")
    return {"status": "200"}


#Route to call the notify function
#This function will trigger a blynk event that will send a push notification to the users mobile alerting them that no movement
#has been detected in a set amount of time. 
@app.route('/dogdetect/notify',methods=['POST'])
def notify():
    blynk.log_event("notify_demo")
    return {"status": "200"}


if __name__ == '__main__':

#Run the Blynk app when the api.py file is run directly. This allows the API calls to trigger events on Blynk
    blynk.run()

#Run API on port 5000, set debug to True
    app.run(host='0.0.0.0', port=5000, debug=True)


    
