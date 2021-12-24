#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: h03.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import threading
import time

semaphore = threading.Semaphore(10)


def run(n):
    semaphore.acquire()
    time.sleep(2)
    print(f'run the thread: {n}')
    semaphore.release()


def main():
    for i in range(50):
        t = threading.Thread(target=run, args=(i,))
        t.start()
    while threading.active_count() != 1:
        pass#print(threading.active_count())
    else:
        print('all thread done')


if __name__ == '__main__':
    main()
