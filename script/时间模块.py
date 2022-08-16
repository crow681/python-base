#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 12:58
# @Author  : wangjun
# @File    : 时间模块.py

import time


t1 = time.time()
print(t1)
print(time.asctime())
print(time.gmtime())
print(time.localtime())
print(time.strftime(('%Y-%m-%d %H:%M:%S'), time.localtime()))
print(time.strptime("30 Nov 00", "%d %b %y"))


