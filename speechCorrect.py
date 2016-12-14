#!/usr/bin/python
# -*- coding: UTF-8 -*-
import speech_recognition as sr
from naoqi import ALProxy
import vr
from os import path
from NAO_Record_correct import record_correct
import wave
import speechRec
#WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "comeOn.wav")
robot_IP = "192.168.1.138"
tts = audio = record = aup = None
tts = ALProxy("ALTextToSpeech", robot_IP, 9559)

def speech_correct_word():
    flag = True
    while flag:
        speechRecCommand = speechRec.speech_recognition()
        try:
            if(speechRecCommand =="no thank you"):
                tts.say("ok!")
                flag = False
            else:
                correctInfo = "you said:"+speechRecCommand+", Am I right?(yes/no)"
                correctInfo = correctInfo.encode('utf-8')
                print(correctInfo)
                tts.say(correctInfo)
                record_correct(robot_IP, robot_PORT=9559)
                WAV_FILE = "/home/nao/record.wav"
                r = sr.Recognizer()
                #m = sr.Microphone()
                m = sr.WavFile(WAV_FILE)
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.record(source)
                    #print("Got it!")
                    try:
                        # recognize speech using Google Speech Recognition
                        checkWord = r.recognize_google(audio)
                        checkWord = checkWord.encode('utf-8')
                        print "you think:"+ checkWord
                        tts.say("you think:"+ checkWord)
                        if( checkWord == "no" or checkWord == "now"):
                            print "Sorry, please say it again..."
                            tts.say("Sorry, please say it again...")
                        else: flag= False
                    except sr.UnknownValueError:
                        print("Oops! Didn't catch that")
                        tts.say("Oops! Didn't catch that")
                    except sr.RequestError as e:
                        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            pass
    return speechRecCommand

