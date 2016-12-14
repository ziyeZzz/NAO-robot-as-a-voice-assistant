import argparse
from naoqi import ALProxy
import time
import os

robot_IP = "192.168.1.138"
tts = audio = record = aup = None 

def record_NAO(robot_IP, robot_PORT=9559):
	global tts, audio, record, aup 
	# ----------> Connect to robot <----------
	tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
	record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
	# ----------> recording <----------
	record.stopMicrophonesRecording()
	print 'start recording...'
	tts.say("start recording...")
	record_path = '/home/nao/record.wav'
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	time.sleep(4)
	record.stopMicrophonesRecording()
	print 'record over'
	tts.say("record over")
        return
	# ----------> playing the recorded file <----------
	#fileID = aup.playFile(record_path, 0.7, 0)
	#cmd = 'scp nao@192.168.1.106:/home/nao/record.wav C:\Users\Administrator\Desktop'
	#os.system(cmd)

        return

