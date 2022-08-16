#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 11:25
# @Author  : wangjun
# @File    : myapp.py
# @explain :
import logging
import mylog

class App:
    def __init__(self):
        mylog.main()    # 日志配置初始化

    def my_app(self, a, b):
        try:
            c = a / b
            return c
        except Exception as e:
            logging.exception(e)

if __name__ == "__main__":
    a = App()
    a.my_app(5, 0)

