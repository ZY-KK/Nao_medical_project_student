from naoqi import ALProxy
import time


class scanCard:
    def scanFunction(self):

        robot_IP = "192.168.1.106"
        barcode = ALProxy('ALBarcodeReader', robot_IP, 9559)
        barcode.subscribe('test_barcode')
        memory = ALProxy('ALMemory', robot_IP, 9559)
        tts = ALProxy("ALTextToSpeech", robot_IP, 9559)
        print "welcome, please show your KELA card and place it in front of my eyes for scanning"
        tts.say("welcome, please show your KELA card and place it in front of my eyes for scanning")
        for i in range(20):
            data = memory.getData("BarcodeReader/BarcodeDetected")
            print data
            if data[0]!="":
                scanResult = data
                tts.say("KELA card scanning is successful")
                print "KELA card scanning is successful"
                break
            time.sleep(1)
        return scanResult
