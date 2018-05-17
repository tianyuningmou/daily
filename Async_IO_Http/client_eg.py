# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: client_eg.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/17 上午11:01

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/17 上午11:01
"""

import aiohttp
import asyncio
import async_timeout


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.baidu.com')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
