#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 21:33
# @Author  : wangjun
# @File    : 异常处理.py

import logging
import traceback

logging.basicConfig(filename='../script/log.log', level=logging.DEBUG)

def my_err():
    try:
        1/0
    except Exception as e:
        logging.exception(e)    # 将运行异常信息存入日志

my_err()
