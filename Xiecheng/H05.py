#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: H05.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import time


def t1():
    while True:
        print('---1---')
        time.sleep(1)
        yield


def t2():
    while True:
        print('---2---')
        time.sleep(1)
        yield


def main():
    t11 = t1()
    t22 = t2()
    while True:
       next(t11)
       next(t22)


if __name__ == '__main__':
    main()
