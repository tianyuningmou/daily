# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: async_download_pic.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/7/20 下午12:15

EMAIL: zhangqing@jingdata.com

VERSION: : #1 
CHANGED By: : tianyuningmou
MODIFIED: : @Time : 2018/7/20 下午12:15
"""

import os
import time
import aiohttp
import asyncio
import requests


class Spider(object):
    def __init__(self):
        self.num = 1
        if '图片' not in os.listdir('.'):
            os.mkdir('图片')
        self.path = os.path.join(os.path.abspath('.'), '图片')
        os.chdir(self.path)

    async def __get_content(self, link):
        async with aiohttp.ClientSession() as session:
            response = await session.get(link)
            content = await response.read()
            return content

    def __get_img_links(self, page):
        URL = 'https://unsplash.com/napi/photos'
        params = {
            'page': page,
            'per_page': 1,
            'order_by': 'latest'
        }
        response = requests.get(URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print('请求失败，状态码：{status_code}'.format(status_code=response.status_code))

    async def __download_img(self, img):
        content = await self.__get_content(img[1])
        with open(img[0] + '.jpg', 'wb') as f:
            f.write(content)
        print('下载第{num}张图片成功'.format(self.num))
        self.num += 1

    def run(self):
        start = time.time()
        for x in range(1, 11):
            links = self.__get_img_links(x)
            tasks = [asyncio.ensure_future(self.__download_img((link['id'], link['links']['download']))) for link in
                     links]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))
        end = time.time()
        print('共运行了{S}秒'.format(S=end-start))


if __name__ == '__main__':
    spider = Spider()
    spider.run()
