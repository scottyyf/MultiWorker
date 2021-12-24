#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Event.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import threading
import time


class WaitForEvent(threading.Thread):
    def __init__(self, event:threading.Event, me,*args, **kwargs):
        self._event = event
        self._me = me
        super(WaitForEvent, self).__init__(*args, **kwargs)

    def run(self) -> None:
        while True:
            if self._event.is_set():
                print(f'[{self._me}]绿灯行...')
                time.sleep(1)
            else:
                print(f'[{self._me}]红灯停...')
                self._event.wait()
                print(f'\033[34;1m绿灯出发\033[0m')


class Lighte(threading.Thread):
    def __init__(self, event:threading.Event, me,*args, **kwargs):
        self._event = event
        self._me = me
        super(Lighte, self).__init__(*args, **kwargs)

    def run(self) -> None:
        count = 0
        while True:
            if count < 5:
                self._event.set()
                print(f'\033[34;1m绿灯亮\033[0m')
            elif count > 10:
                count = 0
            else:
                self._event.clear()
                print(f'\033[41;1m红灯灯亮\041[0m')

            count += 1
            time.sleep(1)


if __name__ == '__main__':
    event = threading.Event()
    light = Lighte(event, '')
    t1 = WaitForEvent(event, 'adi')
    t2 = WaitForEvent(event, 'dazong')
    light.start()
    t1.start()
    t2.start()