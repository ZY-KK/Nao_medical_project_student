#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import speech_recognition as sr
import time
import datetime

#获取文件夹下的音频文件名
starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'D:\PyCharm Community Edition 2016.2.3\untitled\NAOqi\speech'):
    print '%d %s 开始转换' % (i, name)
    #音频分块识别
    r = sr.Recognizer()
    try:
        with sr.WavFile(r'D:\PyCharm Community Edition 2016.2.3\untitled\NAOqi\speech\%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = '19ab0297-0321-4657-83b1-bb1b4f46b3e8'
            IBM_PASSWORD = '8Ey3aH02ZODI'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-US')
            print text
            open(r'D:\PyCharm Community Edition 2016.2.3\untitled\NAOqi\translate\%s.txt' % name, 'a+').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print '%s %d %s 已完成' % (temptime, i, name)
    except Exception as e:
        print e
        temptime = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        print '%s %d %s 未完成' % (temptime, i, name)
        continue
jietime = datetime.datetime.now()
last = jietime - starttime
print 'total time is %s' % last