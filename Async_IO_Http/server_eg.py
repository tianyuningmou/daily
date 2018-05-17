# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: server_eg.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/17 上午11:16

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/17 上午11:16
"""

from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)

    web.run_app(app)
