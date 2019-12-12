#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2019/12/10 22:18

import time
import threading

class MyThread(threading.Thread):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print("the args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

'''
for i in  dir(MyThread):
    print(i)
print('main thread is done....')
'''
