#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: H03.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import time


class Fabnotial(object):
    def __init__(self, left, right, depth=10):
        self._left = left
        self._right = right
        self._depth = depth
        self._current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current <= self._depth:
            self._current += 1
            ret = self._left + self._right
            self._left, self._right = self._right, ret
            return ret

        else:
            raise StopIteration


def main():
    for i in Fabnotial(0, 1, 10):
        time.sleep(0.2)
        print(i, end=' ', sep='')

    f = Fabnotial(0,1)
    r = list(f)
    print(r)
    # environment = 1


if __name__ == '__main__':
    main()
