#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: H02.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import time


class Xrange(object):
    def __init__(self, start, end, step):
        self._start = start
        self._end = end
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            ret = self._start
            self._start += self._step
            return ret
        else:
            raise StopIteration


def main():
    for i in Xrange(1, 1000, 4):
        time.sleep(0.2)
        print(i)


if __name__ == '__main__':
    main()
