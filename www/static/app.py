#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 12/19/2019
# @Email : 1725491705@qq.com
# @software : PyCharm

'''
建立web App
'''
from aiohttp import web
from datetime import datetime

def index(request):
    return web.Response(body=b'<h1>index page</h1>', content_type='text/html')

async def init()