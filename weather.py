#!/usr/bin/python
#coding=utf-8
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup
import re
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.138", 9559)
def check_weather(robot_IP,robot_PORT,place):
	departure_time=[]
	arrival_time=[]
	travel_time=[]
	trains=[]
	price=[]
	price_felxible=''
	browser = webdriver.PhantomJS()
	browser.set_window_size(800, 600)
	browser.get('https://weather.yahoo.com/')
	browser.find_element_by_id("UHSearchBox").clear()
	browser.find_element_by_id("UHSearchBox").send_keys(place)
	#time.sleep(2)
	browser.find_element_by_id("UHSearchBox").send_keys(Keys.ENTER)
	soup = BeautifulSoup(browser.page_source,"html.parser")
	for ele in soup.select('.loc .name'):
		print ele.text
		tts.say((ele.text).encode('utf-8'))
	for ele in soup.select('.loc .region'):
		print ele.text
		tts.say((ele.text).encode('utf-8'))
	for ele in soup.select('.bd .cond'):
		info = "Today's weather:"+ele.text+","+soup.select('.forecast .temperature .hi-c')[0].text+" to "+soup.select('.forecast .temperature .lo-c')[0].text
		print info
		info = info.encode('utf-8')
		tts.say(info)
	#print "Tomorrow's weather:"+soup.select('.forecast .temperature .hi-c')[1].text+" to "+soup.select('.forecast .temperature .lo-c')[1].text
	for ele in soup.select('#mediaweatherdetailsext'):
		print ele.text
		tts.say((ele.text).encode('utf-8'))
	browser.close()
	return

check_weather("192.168.1.138",9559,"Helsinki")
