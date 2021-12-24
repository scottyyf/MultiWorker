#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: h01.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import os
import threading
import random
import time
from threading import Thread, enumerate, Lock, RLock
import sys
import socket


l = RLock()


def recv_msg():
    # while True:
    #     recv_data = udp_sk.recvfrom(1024)
    #     print(recv_data)
    while True:

        l.acquire()
        print('recv msg ----')
        l.acquire()
        l.release()
        l.release()
        time.sleep(0.1)


def send_msg():
    # print('send')
    # while True:
    #     send_data = input('input data:')
    #     udp_sk.sendto(send_data.encode('utf-8'), ('192.168.122.126', 8888))
    for _ in range(5):
        print('attempt to acquire a rlock')
        l.acquire()
        print('send msg ----')
        time.sleep(0.9)
    # show(d)
    # d.val = 50
    # show(d)
    # raise ValueError('send msg exception')


def show(d):
    try:
        val = d.val
    except:
        print('no value yet')
    else:
        print(val)


def main():

    # print('xxxxx00000')
    # udp_sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_sk.bind(("", 8888))
    # data = threading.local()
    # show(data)
    # data.val = 100
    # show(data)
    #
    #os.setpgrp()
    print('ppppp')
    t1 = Thread(target=recv_msg)
    t2 = Thread(target=send_msg)

    # t1.daemon = True
    # t2.daemon = True
    t1.start()
    t2.start()
    print('yyy')
    # t1.join()
    # t2.join()
    # raise ValueError('123')
    # print(threading.active_count())


if __name__ == '__main__':
    main()