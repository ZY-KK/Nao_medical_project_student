#!/usr/bin/env python
# -*-coding:utf-8 -*-

from naoqi import ALProxy
import time
import shelve

class diagnose:
    # def __init__(self):
    # robot ip address
    # robot_IP = "nao.local"
    # robot_PORT = 9559
    tts = None

    def diagnose(self, physical_conditions, robot_IP, robot_PORT,scanResult):
        global tts
        tts = ALProxy('ALTextToSpeech', robot_IP, robot_PORT)
        result = 'I suggest that you can go to ' + physical_conditions
        print  result
        tts.say(result)
        dataFile=result+'.dat'
        dataBase=shelve.open(dataFile)
        if 'KELA_Card' not in dataBase:
            KELA_Card=[]
        else:
            KELA_Card=dataBase['KELA_Card']
            KELA_Card.insert(0,{
                'KELA': scanResult
            })

        dataBase['KELA_Card']=KELA_Card

        dataBase.close()
        dataBase=shelve.open(dataFile)
        dataList=dataBase.get('KELA_Card',[])
        length=len(dataList)
        result='There are'+length+'people in queue before you'
        tts.say(result)
        print 'There are %s people in queue before you'%length


