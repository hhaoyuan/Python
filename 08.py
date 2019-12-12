#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2019/12/10 22:00

import time
import threading

def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(6)
    print('End loop 2 at:', time.ctime())


def loop3():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print('End loop 3 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=( ))
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=( ))
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=( ))
    t3.setName("THR_3")
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print('正在执行的线程名字是 :  {0}'.format(thr.getName()))

    print("正在运行的子线程数量为: {0}".format(threading.active_count()))
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()