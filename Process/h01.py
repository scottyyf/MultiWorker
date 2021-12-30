#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: h01.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import multiprocessing
import os
import subprocess
import time


def test1():
    while True:
        print('test1 running')
        time.sleep(1)


def test2():
    while True:
        print('test2 running')
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1, daemon=True)
    p2 = multiprocessing.Process(target=test2, daemon=True)
    p1.start()
    p2.start()
    # os._exit(0)
    main_print()


def main_print():
    n = 0
    while True:
        if n >= 100:
            break

        print(f'main process print {n}')
        n += 1
        time.sleep(1)


if __name__ == '__main__':
    main()
