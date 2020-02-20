#!/usr/bin/env python
# -*- coding:utf-8 -*-


from naoqi import ALProxy
import os
import time

from speech_recognition_by_Nao import speechToText


class judgement:
    def judgementPro(self):
        robot_IP = "192.168.1.106"
        tts = ALProxy("ALTextToSpeech", robot_IP, 9559)
        record = ALProxy("ALAudioRecorder", robot_IP, 9559)
        stt = speechToText()

        judgeResultFile = ("/home/nao/nao_medical_diagnose/diagnose_test/judgeResult.wav")
        channels = [0, 0, 1, 0]
        record.startMicrophonesRecording(judgeResultFile, 'wav', 16000, channels)
        time.sleep(2)
        record.stopMicrophonesRecording()
        print "record over"

       # downloadFile = remoteFile()
       # downloadFile.getRemoteFile("/home/nao/diagnose_test/judgeResult.wav", "./diagnose_test/judgeResult.wav")
        judgeResult = stt.fileRecognizer(judgeResultFile)
        return judgeResult
