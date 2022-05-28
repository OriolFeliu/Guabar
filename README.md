<img src="https://user-images.githubusercontent.com/106244659/170769917-426e1645-2c16-4824-b882-c759c457b869.jpg" align="right" width="300" alt="header pic"/>

# Guabar-Forever

The smartbartender you need.

# Table of Contents
   * [What is this?](#what-is-this)
   * [Description](#description)
   * [Electronic Components](#electronic-components)
   * [Hardware Schematics](#hardware-schematics)
   * [Software Architecture](#software-architecture)
        * [Interactive App](#interactive-app)
            * [Menu selector](#menu-selector)
            * [Voice Recognition](#voice-recognition)
        * [Face Detection](#face-detection)
        * [Servo Movement](#servo-movement) 
   * [3D Pieces](#3d-pieces)
   * [Amazing-Contributions](#amazing-contributions)
   * [Bibliography](#bibliography)
   * [Authors](#authors)
   * [Video](#video)
   
# What is this?

This project consists in a robot arm that makes you a drink using dispensing fountains. Through a camera, we use computer vision so the robot can recongize and grab the cup and give it directly to your hand.

It's made from 3D printed components and uses Servo motors and a Raspberry Pi. The budget of this project is 100 €. 

# Description

The robot arm has 3 joints and it is capable of grabbing a cup, put liquids in it and git it directly to your hand.

This Git contains the code to make the arm work using a Raspberry Pi.

The robot can do the following things:
1. Grab cup.
2. Using a microphone, listen to the order by voice from the user.
3. Push the dispenser with the cup to put liquids in it.
4. Move the cup to your hand using computer vision.

# Electronic Components
- Raspberry Pi 4
- Micro servo SG90
- Adafruit Servo FeatherWing (16 channels PWM) 
- Servomotor 3001HB
- Webcam
- Power Supply Raspberry Pi 4, USB-C, 5.1V 3A

# Hardware schematics
The following figure is the hardware schematics of the robot. Also voice recognition is used from a computer through an app that controls what the user orders.
![hardwareSchematics](https://user-images.githubusercontent.com/106244659/170773151-a1dbc667-78f6-4d93-a71c-11d20636b683.png)

# Software Architecture
We have different software modules:
<img width="258" alt="image" src="https://user-images.githubusercontent.com/106244659/170774332-21024a7d-4040-4f5a-a542-79ea23af9afb.png">

## Interactive App
We have created an interactive web app to place the different orders to the bartender robot. It is connected to the Raspberry using SSH and different parameters are used to accomplish the desired actions. This app is developed in Flask and Paramiko is used to create the SSH connection. 

### Menu Selector
To have a more than one option to ask for an order, we have created a menu selector on the app. Basically, it gives you the pictures of the different available drinks and you just need to select the ones you want and submit the order.

### Voice Recognition
The microphone provided to the raspberry to process the audio it takes to recognize the orders matching every word with a predefined ones, the different drinks available.

We use speech_recognition  as a library to do the voice recognition program.

## Face Detection 
As the last module we take data from the web camera the robot it has on the top to process the video frames to detect faces, that faces are detected with the propose of let know the robot if the person is on the right or on the left to move it selves.

We use the library cv2 to capture and process the camera images. And face_detection to do the face detection at the images.

## Servo Movement
We defined a few functions that sets the different types of movements the robot have, one for open the hand, other for close it, etc.

# 3D Pieces
Gears:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170775776-4c2a5e58-c742-41aa-97ed-563347825422.png">

Horizontal arm: that is what moves out.
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170775591-072cf110-f8c0-493e-a6bf-280e57b068f7.png">

Hand of the robot
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170776014-36a1b147-d73f-4c8c-8cba-8bf5d9681690.png">

Structural arm
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170776139-843719ca-7420-4bfb-af77-6812d08d2c70.png">


# Amazing contributions

A robot that acts as a bartender, just speak with him as confident as you can. You won’t notice that is a robot, it will be your friend.
You can order to him in 2 different ways, the first one consist in select the order with a menu in app and the other consists in order by the voice as if you are talking with a bartender.
Guabar-Forever track your face to recognize where you are and serves the drink as near as possible to you.

# Bibliography
This project has been inspired by the following project:
https://www.hackster.io/hackershack/smart-bartender-5c430e

Information to know how to do the project:
https://learn.adafruit.com/16-channel-pwm-servo-driver
https://pypi.org/project/face-detection/
https://opencv.org/releases/
https://pypi.org/project/SpeechRecognition/
https://www.paramiko.org/
https://flask.palletsprojects.com/en/2.1.x/
https://www.raspberrypi.com/documentation/


# Authors
Oriol Feliu Juarez,
Ivan Cañas Martin,
Oscar Moreno Ramos

# Video
Coming soon
