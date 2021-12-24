#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: h02.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import threading
import time

def pess(args):
    print(args)

threading.excepthook = pess

lock = threading.Lock()
count = 0
con = threading.Condition(lock)


class Producer(threading.Thread):
    def run(self) -> None:
        global count
        while True:
            if con.acquire():
                if count > 6000:
                    print('wait: producer hole lock? ', lock.locked())
                    print('producer wait ....')
                    con.wait()
                    print('producer after wait')
                else:
                    count += 100
                    print(f'notify: produce and count is {count}')
                    con.notify()
                    print(f'notify: produce and count is {count}')
                con.release()
                time.sleep(2)


class Consume(threading.Thread):
    def run(self) -> None:
        global count
        while True:
            with con:
                con.wait_for(self.predicate(con))

                # if count < 800:
                #     print('wait: consumer hold lock?', lock.locked())
                #     print('consumer wait ....')
                #     con.wait()
                #     print('consumer after wait')
                # else:
                #     count -= 100
                #     print(f'notify: Consume and count is {count}')
                #     con.notify()
                #     print(f'notify: Consume and count is {count}')
                # time.sleep(2)

    def predicate(self, conn):
        def t():
            global count
            if count >= 6000:
                print(f'case: Consume and count is {count}')
                count -= 200
                conn.notify()
                return True

            # count -= 100
            # conn.notify()
            time.sleep(2)
            print(f'notify: Consume and count is {count}')
            return False
        return t


if __name__ == '__main__':
    p = Producer()
    c = Consume()
    try:
        p.start()
        c.start()
    except:
        pass