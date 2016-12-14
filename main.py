#!/usr/bin/python
# -*- coding: UTF-8 -*-
import speechRec as sr
import speechCorrect as sc
import vr
import weather
from naoqi import ALProxy
import argparse


robot_IP = "192.168.1.138"
robot_PORT = "9559"
tts = ALProxy("ALTextToSpeech", robot_IP, 9559)
print "Welcome to voice assistant.(keywords:train tickets, weather)"
tts.say("Welcome to voice assistant.(keywords:train tickets, weather)")
while True:
    command = sc.speech_correct_word()
    command = command.encode('utf-8')
    NAO_SAY = 'yes'+command
    print type(command)
    print NAO_SAY 
    tts.say(NAO_SAY)
    if(command == "train tickets" or command =="train ticket"):
        print "ok! Please tell me departure date of the train:"
        print "-----Year(ex,2016)-------"
        year = sc.speech_correct_word()
        print "-----Month(ex,2)---------"
        month = sc.speech_correct_word()
        print "-----Date(ex,20)---------"
        date = sc.speech_correct_word()
        print "---Departure station(ex,Vaasa)--------"
        departureStation = sc.speech_correct_word()
        print "---Destination station(ex,Helsinki)---"
        destinationStation = sc.speech_correct_word()
        day=date+".0"+month+"."+year
        vr.train_tickets(robot_IP,robot_PORT,departureStation,destinationStation,day)
    if(command == "weather"):
        print "ok! Please tell me the place:"
        tts.say("ok! Please tell me the place:")
        place = sc.speech_correct_word()
        weather.check_weather(robot_IP,robot_PORT,place)

