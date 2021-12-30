#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: CopyDir.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import multiprocessing
import os
import time
import sys


def copy_file(src, dest, q):
    # print(f'-'*10, src)
    time.sleep(2)
    q.put(src)


def main():
    old_folder_name = '/tmp'
    try:
        os.mkdir(old_folder_name)
    except:
        pass

    files= os.listdir(old_folder_name)

    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool()
    for f in files:
        po.apply_async(copy_file, args=(f, 'p', q))

    po.close()
    # po.join()
    while True:
        f = q.get()
        print(100, end=" ")


if __name__ == '__main__':
    main()
