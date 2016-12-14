#!/usr/bin/python
#coding=utf-8
from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

def train_tickets(robot_IP,robot_PORT,departureStation,destinationStation,day):
        tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
        departure_time=[]
        arrival_time=[]
        travel_time=[]
        trains=[]
        price=[]
        price_felxible=''
        browser = webdriver.Firefox()
        browser.get('https://www.vr.fi/cs/vr/en/frontpage')
        soup = BeautifulSoup(browser.page_source,"html.parser")
        browser.find_element_by_id("tabs1_station").send_keys(departureStation)
        browser.find_element_by_id("tabs1_stationdestination").send_keys(destinationStation)
        browser.find_element_by_id("tabs1_startDate").clear()
        browser.find_element_by_id("tabs1_startDate").send_keys(day)
        browser.find_element_by_id("tabs1_submitbutton1").click()
        soup = BeautifulSoup(browser.page_source,"html.parser")
        time.sleep(3)

        for ele in soup.select('.tripStartDomestic'):
                departure_time.append(ele.text)
        print "End1"
        for ele in soup.select('.tripEndDomestic'):
                arrival_time.append(ele.text)	
        print "End2"
        for ele in soup.select('.tripDurationDomestic'):
                travel_time.append(ele.text)
        print "End3"
        for ele in soup.select('.tripTrainTypesDomestic'):
                text = ele.text
                p = re.compile('\s+')
                line=re.sub(p,' ',text)
                trains.append(line)
        print "End4"
        for ele in soup.select('.tripPriceFrom'):
                text = ele.text
                p = re.compile('\s+')
                line=re.sub(p,' ',text)
                price.append(line)
        print "End5"
        train_number = str(len(departure_time))
        print "From "+departureStation+" to "+destinationStation+", the date is "+day
        print "I found "+train_number+" trains"
        i=0
        while i<len(departure_time):
                j=i*2
                k=i*2+1
                print "The " + str(i+1)+" train:"
                tts.say("The " + str(i+1)+" train:")
                print "Departure_time:"+str(departure_time[i])+" Arrival_time:"+str(arrival_time[i])
                tts.say("Departure_time:"+str(departure_time[i])+" Arrival_time:"+str(arrival_time[i]))
                print trains[i]
                tts.say(trains[i])
                print "Following are prices info:"
                tts.say("Following are prices info:")
                print price[i]
                tts.say(price[i])
                print "\n"
                i=i+1
        browser.close()
        return

