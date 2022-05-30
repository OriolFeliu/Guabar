<img src="https://user-images.githubusercontent.com/106244659/170769917-426e1645-2c16-4824-b882-c759c457b869.jpg" align="right" width="300" alt="header pic"/>

# Guabar-Forever

The smart bartender you need.

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

This project consists of a robot arm that makes drinks using dispensing fountains. Through a camera, computer vision is used so the robot can recognize and grab the cup and give it directly to your hand.

It's made from 3D printed components and uses Servo motors and a Raspberry Pi. The budget for this project is 100 €. 

# Description

The robot arm has 3 joints and it is capable of grabbing a cup, putting liquids in it and giving it directly into your hand.

This Git contains the code to make the arm work using a Raspberry Pi.

The robot can do the following things:
1. Grab a cup.
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
The following figure is the hardware schematics of the robot. Also, voice recognition is used from a computer through an app that controls what the user orders.

![hardwareSchematics](https://user-images.githubusercontent.com/106244659/170773151-a1dbc667-78f6-4d93-a71c-11d20636b683.png)

# Software Architecture
The following image shows different software modules:

<img width="258" alt="image" src="https://user-images.githubusercontent.com/106244659/170774332-21024a7d-4040-4f5a-a542-79ea23af9afb.png">

## Interactive App
An interactive web app has been created to place the different orders for the bartender robot. It is connected to the Raspberry using SSH and different parameters are used to accomplish the desired actions. This app is developed in Flask and Paramiko is used to create the SSH connection. 

### Menu Selector
To have more than one option to ask for an order, a menu selector appears in the app. Basically, it gives the user pictures of the different available drinks and is just required to select the ones that want and submit the order.

### Voice Recognition
An external microphone is required to use voice recognition. In our case, we use the microphone integrated into our computers. 

The code matches the voice orders with predefined ones. If it doesn't find any match, the program will respond that it didn't understand the order. It will also recognize the different requested available drinks.

The speech_recognition library is used to do the voice recognition sub-program.

## Face Detection
For the last module, data is taken through an external camera placed on top of the robot to process so it can detect faces. The robot arm will move right or left depending on where the person is standing.

The cv2 library is used to capture and process the camera images. The face_detection library is used to do the face detection on the frames taken from the camera.

## Servo Movement
A few functions have been created to set the different types of movements the robot can do, like opening or closing its hand, moving the hand to the desired position, etc.

# 3D Pieces
Gears:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170775776-4c2a5e58-c742-41aa-97ed-563347825422.png">

Horizontal arm:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170775591-072cf110-f8c0-493e-a6bf-280e57b068f7.png">

Hand of the robot:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170776014-36a1b147-d73f-4c8c-8cba-8bf5d9681690.png">

Structural arm:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170776139-843719ca-7420-4bfb-af77-6812d08d2c70.png">


# Amazing contributions

A robot that acts as a bartender, just speak with him as confidently as you can. You won’t notice that it is a robot, it will be your server.

You can order him in 2 different ways:
- Select the order through the menu found in the web app.
- Order using your voice as if you were talking with a real bartender.

Guabar-Forever tracks your face to recognize where you are and serves the drink as near as possible to you.

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
- Oriol Feliu Juárez
- Ivan Cañas Martin
- Oscar Moreno Ramos

- [Contributors to Guabar](https://github.com/OriolFeliu/Guabar/graphs/contributors)

# Video
Coming soon
