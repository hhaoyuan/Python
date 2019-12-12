#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2019/12/9 14:47

#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=() )
t1.start()

time.sleep(1)
print("Main thread end")