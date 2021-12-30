#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: deadlock.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from multiprocessing import Process, Queue


def f(q):
    q.put('X' * 10)


if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    obj = queue.get()
    p.join()  # this deadlocks
    print(obj)
