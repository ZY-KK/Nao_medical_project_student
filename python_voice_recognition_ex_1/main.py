#!/usr/bin/env python
# -*-coding:utf-8 -*-


from diagnose import diagnose
from keywords_finding import keywords_finding
from medical_tree import node, tree
from speech_recognition_by_Nao import speechToText
from naoqi import ALProxy
import time
from scanModule import scanCard
from judgementClass import judgement

if __name__ == '__main__':
    robot_IP = "192.168.1.106"
    # robot_PORT = 9559
    """create nodes"""
    hospital = node('Hospital')
    internalDepartment = node('Internal Department')
    surgicalDepartment = node('Surgical Department')
    fever = node('fever')
    headache = node('headache')
    bleeding = node('bleeding')
    fall = node('fall')
    stomach=node('stomach')
    """connect the nao robot"""
    tts = ALProxy("ALTextToSpeech", robot_IP, 9559)
    record = ALProxy("ALAudioRecorder", robot_IP, 9559)

    """add the value"""
    hospital.addChildren(internalDepartment)
    hospital.addChildren(surgicalDepartment)
    internalDepartment.addChildren(fever)
    internalDepartment.addChildren(headache)
    internalDepartment.addChildren(stomach)
    surgicalDepartment.addChildren(bleeding)
    surgicalDepartment.addChildren(fall)

    internalDepartment.addFather(hospital)
    surgicalDepartment.addFather(hospital)

    fever.addFather(internalDepartment)
    headache.addFather(internalDepartment)
    stomach.addFather(internalDepartment)
    bleeding.addFather(surgicalDepartment)
    fall.addFather(surgicalDepartment)


    tree = tree(hospital)

    global flag, record_filePath, recognition_result
    record_filePath = ("/home/nao/nao_medical_diagnose/diagnose_test/record.wav")
    judgement = judgement()
    scan=scanCard()
    scanResult=scan.scanFunction()
    print scanResult
    flag = False
    while flag == False:

        """get the record.wav recognition result"""
        stt = speechToText()
        stt.record_Nao(robot_IP, record_filePath)

        recognition_result = stt.fileRecognizer("/home/nao/nao_medical_diagnose/diagnose_test/record.wav")
        print recognition_result
        tts.say(recognition_result[:-1].encode('utf-8'))

        """To judge if the result right"""
        print "Is the result right, yes or no"
        tts.say("Is the result right, yes or no")



        judgeResult = judgement.judgementPro()
        print judgeResult
        tts.say(judgeResult[:-1].encode('utf-8'))
        """To judge the process should continue or not """
        if judgeResult == "yes":
            flag = True
            keyf = keywords_finding()
            matchWords = keyf.find_keyword(recognition_result)
            print recognition_result
            if recognition_result == "":
                flag = False
                tts.say("Sorry, I cannot hear clearly")

            else:
                word = [matchWord.encode('utf-8') for matchWord in matchWords]
                print word[0]
                diagnoseResult = tree.findFather(hospital, word[0])
                if diagnoseResult == None:
                    flag = False
                    tts.say("Sorry, I cannot find any suggestion")

                else:
                    dia = diagnose()
                    dia.diagnose(diagnoseResult, robot_IP, 9559,scanResult)
                    time.sleep(1)
                    print "Do you want continue, yes or no?"
                    tts.say("Do you want continue, yes or no?")
                    judgeForNext = judgement.judgementPro()
                    if judgeForNext == "Yes.":
                        tts.say(judgeForNext[:-1].encode("utf-8"))
                        flag = False
                    else:
                        flag = True
                        print "Thanks for using, goodbye!"
                        tts.say("Thanks for using, goodbye!")

        else:
            flag = False
