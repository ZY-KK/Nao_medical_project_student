#!/usr/bin/env python
# -*-coding:utf-8 -*-
import argparse
from naoqi import ALProxy
import time
import os
import speech_recognition as sr
import datetime

# robot ip address
robot_IP = ""

tts = audio = record = aup = None


def record_Nao(robot_IP, robot_PORT=""):
    global tts, audio, record, aup
    tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)

    record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
    # ------>check the recorder if it is working<------#
    record.stopMicrophonesRecording()
    print'please describe where you are uncomfortable'
    tts.say("please describe where you are uncomfortable")
    # ------>to store record files<------#
    record_filePath = ("")
    channels = (0, 0, 1, 0)

    record.startMicrophonesRecording(record_filePath, 'wav', 16000, channels)
    time.sleep(10)
    record.stopMicrophonesRecording()


#
# divide two function
# in main function if we want to use function
# we should add a loop and call functionon


def fileRecognizer(filePath):
    recognizer = sr.Recognizer()
    i = 1
    try:
        with sr.WavFile("#-->filePath<--#") as source:
            audio = recognizer.record(source)
            # ------>speech recognition API<------#
            # ------>IBM speech recognition API<------#
            IBM_USERNAME = ''
            IBM_PASSWORD = ''

            recognitionText = recognizer.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD,
                                                       language='en-US')
            print recognitionText
    except Exception as e:
        print e
        temptime = datetime.datetime.time().strftime('%Y%m%d %H:%M:%S')
        print '%s %d %s not finish' % (temptime, i, filePath)
