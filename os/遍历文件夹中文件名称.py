#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/29 16:18
# @Author  : wangjun
# @File    : 遍历文件夹中文件名称.py
# @explain : os.walk()

import os
def func(dirname):
    for root, dirs, files in os.walk(dirname):
        # 列出所有文件
        for name in files:
            print(os.path.join(root, name))
        # 列出所有文件夹及文件
        for name in dirs:
            print(os.path.join(root, name))


dirname = 'D:\Work_bmsoft\Jmeter_Script'
func(dirname)