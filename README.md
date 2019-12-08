# IoT-Safety-Cane

UCI Project Course: CS 147 IoT Sofware and System

Hardware:
Raspberry Pi 4; Arduino Uno, GPS sensor, Accelerometer, Button, and LED light

Software: 
Twilio for SMS, ThingSpeak for reading/writing out GPS coordinates to the cloud, C/C++ (Arduino IDE), and Python (on Raspbian OS)

The Uno collects all the sensor data and sends a message to the Pi via serial.
The Pi connects to wifi and sends the GPS data to ThingSpeak.
The Pi also sends out SMS messages via Twilio.

Scenario 1 - Cane detects fall and the user actually has fallen: 
Uno sends the GPS coordinates and a "Fall" message to the Pi.
The Pi uploads the GPS coordinates to ThingSpeak 
The Pi also sends an SMS message to an emergency contact about the fall and includes the GPS coordinates

Scenario 2 - Cane detects fall and the user didn't fall (cane slipped/fell by itself): 
Uno sends the GPS coordinates and a "Fall" message to the Pi.
The Pi uploads the GPS coordinates to ThingSpeak and it also sends out an SMS message about the fall and includes the GPS coordinates
User can press a button (connected via Uno) that would cause the Uno to send a "False Alarm" message to the Pi.
The Pi sees the "False Alarm" message and will send another SMS saying that it was a false alarm

All the hardware was placed into an enclosure made from cardboard and attached to a cane.
Images: https://drive.google.com/drive/folders/1Wu1xnbyBWifSeKqjIWqvXnAmfbittX8y?usp=sharing

Please see the Project Report doc and/or the Safety Cane PPT for more details
This project was done in a team of two
