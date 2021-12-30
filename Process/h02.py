#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: h02.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import multiprocessing
import random
import time


def put_data_to_queue(q: multiprocessing.Queue, nums):
    while True:
        num = random.choice(nums)
        q.put(num)
        print(f'put num {num} to queue...')
        time.sleep(6)


def get_data_from_queue(q: multiprocessing.Queue):
    while True:
        ret = q.get()
        print(f'get data {ret} from queue...')
        time.sleep(2)


def main():
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=put_data_to_queue,
                                 args=(queue, [1, 2, 3, 4]),
                                 daemon=True)
    p2 = multiprocessing.Process(target=get_data_from_queue, args=(queue,),
                                 daemon=True)
    p1.start()
    p2.start()
    time.sleep(100)


if __name__ == '__main__':
    main()
