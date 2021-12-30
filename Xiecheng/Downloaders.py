#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Downloaders.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""

import shutil
import gevent
from gevent import monkey

monkey.patch_all()

import requests

url1 = 'https://rpic.douyucdn.cn/live-cover/roomCover/2021/12/15/54f9e17da08174b3c86b947fda697b4d_big.png/dy1'
url2 = 'https://rpic.douyucdn.cn/live-cover/roomCover/2021/11/03/dbac8883420728c6c796db3debe86223_big.png/dy1'


def main(url, dst):
    resp = requests.get(url, stream=True)
    if resp.status_code == 200:
        with open(f'{dst}.png', 'wb') as f:
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, f)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(main, url1, '1'),
        gevent.spawn(main, url2, '2')
        ])
