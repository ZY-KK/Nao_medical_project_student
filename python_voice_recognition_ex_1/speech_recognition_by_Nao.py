#!/usr/bin/env python
# -*-coding:utf-8 -*-
import argparse
from naoqi import ALProxy
import time
import os
import speech_recognition as sr
import datetime


class speechToText:
    # robot ip address

    tts = audio = record = aup = None


    def record_Nao(self,robot_IP, record_filePath):
        global tts, audio, record, aup
        tts = ALProxy("ALTextToSpeech", robot_IP, 9559)

        record = ALProxy("ALAudioRecorder", robot_IP, 9559)
        # ------>check the recorder if it is working<------#
        record.stopMicrophonesRecording()
        print'what kind of sickness do you have?'
        tts.say("what kind of sickness do you have?")
        # ------>to store record files<------#
       # record_filePath = ("/home/nao/diagnose_test/record.wav")
        channels = [0, 0, 1, 0]

        record.startMicrophonesRecording(record_filePath, 'wav', 16000, channels)
        time.sleep(5)
        record.stopMicrophonesRecording()
        print "record over"


    #
    # divide two function
    # in main function if we want to use function
    # we should add a loop and call functionon


    def fileRecognizer(self,filePath):
        # remoFile= remoteFile()
        # remoFile.getRemoteFile()

        recognizer = sr.Recognizer()
        i = 1
        try:
            with sr.WavFile(filePath) as source:
                audio = recognizer.record(source)
                # ------>speech recognition API<------#
                # ------>IBM speech recognition API<------#


                recognitionText = recognizer.recognize_bing(audio, key="3742c885403e4d848f53ccf6a0e9cf0e", language='en-US')
                #print recognitionText
                return recognitionText
        except Exception as e:
            print e
            #temptime = datetime.datetime.time().strftime('%Y%m%d %H:%M:%S')
            #print '%s %d %s not finish' % (temptime, i, filePath)

