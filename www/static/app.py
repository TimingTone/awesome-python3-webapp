#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 12/19/2019 1241
# @Email : 1725491705@qq.com
# @software : PyCharm

'''
建立web App
'''
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time                #asyncio 是用来编写 并发 代码的库，使用 async/await 语法
from aiohttp import web
from datetime import datetime

def index(request):
    return web.Response(body=b'<h1>My first Web App AWesome page</h1>', content_type='text/html')

async def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 9000)
    await site.start()
    print('服務器啓動成功')


loop = asyncio.get_event_loop()     #获取当前事件循环。 如果当前 OS 线程没有设置当前事件循环并且 set_event_loop() 还没有被调用，asyncio 将创建一个新的事件循环并将其设置为当前循环
loop.run_until_complete(init())     #运行直到init()被完成
loop.run_forever()                  #运行直到stop()被调用,没有stop()则永远运行直到终止程序启动
