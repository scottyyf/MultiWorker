#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: H01.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import time
from collections.abc import Iterator
from collections.abc import Iterable


class ClassMeta(object):
    def __init__(self):
        self.names = ['a', 'b', 'c']
        self._loc = 0

    def __iter__(self):
        return self

    def __next__(self):
        time.sleep(1)
        if self._loc < len(self.names):
            ret = self.names[self._loc]
            self._loc += 1
            return ret
        else:
            raise StopIteration

class CIter(object):
    def __init__(self, obj):
        self._obj = obj
        self._cursor = 0

    # def __iter__(self):
    #     pass

    def __next__(self):
        if self._cursor < len(self._obj.names):
            ret = self._obj.names[self._cursor]
            self._cursor += 1
            return ret
        else:
            raise StopIteration


def main():
    c = ClassMeta()
    for i in c:
        print(i)
    # print(isinstance(c, Iterator))
    # print(isinstance(c, Iterator))
    # print(next(iter(c)))


if __name__ == '__main__':
    main()
