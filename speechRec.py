#!/usr/bin/python
# -*- coding: UTF-8 -*-
import speech_recognition as sr
import vr
from naoqi import ALProxy
from os import path
from NAO_Record import record_NAO
import wave
#WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "comeOn.wav")
robot_IP = "192.168.1.138"
tts = audio = record = aup = None
tts = ALProxy("ALTextToSpeech", robot_IP, 9559)
def speech_recognition():
    try:
	global speechRecWord_rec
	print("you can say now...")
	tts.say("you can say now...")
        record_NAO(robot_IP, robot_PORT=9559)
        WAV_FILE = "/home/nao/record.wav"
        r = sr.Recognizer()
        #m = sr.Microphone()
        m = sr.WavFile(WAV_FILE)
        #print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold
            #print("Set minimum energy threshold to {}".format(r.energy_threshold))
            audio = r.record(source)
            #print("Got it!")
            try:
                # recognize speech using Google Speech Recognition
                speechRecWord_rec = r.recognize_google(audio)
                print speechRecWord_rec
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
		tts.say("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
    return speechRecWord_rec
