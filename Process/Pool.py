#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Pool.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from multiprocessing import Pool
import multiprocessing
import os, time, random


def worker(msg):
    t_start = time.monotonic()
    print(f'start to execute, pid is {os.getpid()}')
    time.sleep(1)
    # print(multiprocessing.current_process(), '00000')
    t_stop = time.monotonic()
    print(msg, f'finished, last for {t_stop-t_start} s')


po = Pool(3) # 最多3个


def main():
    for i in range(0, 10):
        po.apply_async(worker, (i,))

    print('------start------')
    po.close()
    # po.terminate()
    po.join()
    print('------end--------')


if __name__ == '__main__':
    main()
