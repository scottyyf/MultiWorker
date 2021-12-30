#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Gevent.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import gevent
import time
from gevent import monkey


monkey.patch_all()


def test(n):
    num = 0
    while True:
        print(f'-----{num} {n}-----')
        num += 1
        time.sleep(0.5)


def main():
    g1 = gevent.spawn(test, 1)  # 返回greenlet
    g2 = gevent.spawn(test, 2)

    g1.join()
    g2.join()


if __name__ == '__main__':
    main()
