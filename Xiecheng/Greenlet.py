#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Greenlet.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from greenlet import greenlet
import time


def t1():
    while True:
        print('-----1-----')
        g2.switch()
        time.sleep(0.5)


def t2():
    while True:
        print('-----2-----')
        g1.switch()
        time.sleep(0.5)


g1 = greenlet(t1)
g2 = greenlet(t2)


def main():
    g1.switch()


if __name__ == '__main__':
    main()
