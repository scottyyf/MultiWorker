#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: H04.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


def main():
    left, right, ret = 0, 1, 1
    steps = 10
    current_step = 0
    while current_step <= steps:
        ret = left + right
        left, right = right, ret
        rets = yield ret
        print(rets)
        current_step += 1


if __name__ == '__main__':
    # for i in main():
    #     print(i, end=' ', sep='')
    # ret = [x for x in main()]
    # print(ret)
    m = main()
    print(next(m))
    m.send(12)
