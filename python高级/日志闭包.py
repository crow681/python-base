#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 17:29
# @Author  : wangjun
# @File    : 日志闭包.py
# @explain :

import logging

def log(func):
    # 创建自定义的记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # 添加处理器
    handler = logging.FileHandler(filename='../script/log.log', encoding='utf=8', mode='a')
    handler.setLevel(logging.DEBUG)
    # 添加格式器
    fm = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 对处理器进行格式化
    handler.setFormatter(fm)
    # 添加处理器至记录器中
    logger.addHandler(handler)

    def inner(*args):
        res = func(*args)
        logger.debug('4444')
        return res
    return inner()

@log
def myfuc(a):
    c = a
    return print(c)


myfuc(2)