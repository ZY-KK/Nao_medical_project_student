#!/usr/bin/env python
# -*-coding:utf-8 -*-

from naoqi import ALProxy
import time

# robot ip address
robot_IP = ""

tts = None

def diagnose(physical_conditions, robot_IP, robot_PORT):
    global  tts
    tts=ALProxy('ALTextToSpeech', robot_IP, robot_PORT)
    print """print diagnose result"""
    tts.say("""diagnose result""")

