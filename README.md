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
            * [Voice Recognition](#voice-recognition)
            * [Menu selector](#menu-selector)
        * [Face Detection](#face-detection)
        * [Servo Movement](#servo-movement) 
   * [3D Pieces](#3d-pieces)
   * [Amazing-Contributions](#amazing-contributions)
   * [Bibliography](#bibliography)
   * [Authors](#authors)
   * [Video](#video)
   
# What is this?

This proyect consists in make a robot with 100€ of budget. In this case using computer vision to do the movements of the robot.

# Description

Guabar is a robot arm that serves drinks. It has 3 joints and it is capable of grabbing a cup, put liquids in it and git it directly to your hand.

In this Git there's the code to make the arm work. This code is used in a Raspberry Pi.

1. Grab cup.

2. Push the dispenser with the cup to put liquids in it.

3. Move the cup to your hand using computer vision.

# Electronic Components
Raspberry Pi 4
Micro servo SG90
Adafruit Servo FeatherWing (16 channels PWM) 
Servomotor 3001HB
Webcam
Power Supply Raspberry Pi 4, USB-C, 5.1V 3A


# Hardware schematics
That is our the hardware schematics of our robot but we use voice recognition too from a computer doing it with an app that is who controls what we order.
![hardwareSchematics](https://user-images.githubusercontent.com/106244659/170773151-a1dbc667-78f6-4d93-a71c-11d20636b683.png)

# Software Arquitecture
We have some differents software modules:
<img width="258" alt="image" src="https://user-images.githubusercontent.com/106244659/170774332-21024a7d-4040-4f5a-a542-79ea23af9afb.png">

## Interactive App
We create an interactive app to do the differents orders to the bartender.
This is connected to the raspberry using ssh and we give the differents parameters to do what we want.

### Voice Recognition
The module of voice recognition consits in using 

### Menu Selector

## Face Detection

## Servo Movement

# 3D Pieces

<img width="197" alt="image" src="https://user-images.githubusercontent.com/106244659/170775776-4c2a5e58-c742-41aa-97ed-563347825422.png">

<img width="340" alt="image" src="https://user-images.githubusercontent.com/106244659/170775591-072cf110-f8c0-493e-a6bf-280e57b068f7.png">

<img width="536" alt="image" src="https://user-images.githubusercontent.com/106244659/170776014-36a1b147-d73f-4c8c-8cba-8bf5d9681690.png">

<img width="563" alt="image" src="https://user-images.githubusercontent.com/106244659/170776139-843719ca-7420-4bfb-af77-6812d08d2c70.png">


# Amazing contributions

A robot that acts as a bartender, just speak with him as confident as you can. You won’t notice that is a robot, it will be your friend.
You can order to him in 2 different ways, the first one consist in select the order with a menu in app and the other consists in order by the voice as if you are talking with a bartender.
Guabar-Forever track your face to recognize where you are and serves the drink as near as possible to you.

# Bibliography

# Authors
Oriol Feliu Juarez
Ivan Cañas Martin
Oscar Moreno Ramos
# Video
Coming soon
