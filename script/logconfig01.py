#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 11:53
# @Author  : wangjun
# @File    : logconfig01.py
# @explain :

import logging
import logging.config

# def mylog():
#     """
#     自定义组件输出日志
#     :return:
#     """
#     # 创建自定义的记录器
#     logger = logging.getLogger('显式代码配置')
#     logger.setLevel(logging.DEBUG)
#     # 添加处理器
#     handler = logging.FileHandler(filename='../script/log.log', encoding='utf-8', mode='a')
#     handler.setLevel(logging.DEBUG)
#     # 添加格式器
#     fm = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#
#     # 对处理器进行格式化
#     handler.setFormatter(fm)
#     # 添加处理器至记录器中
#     logger.addHandler(handler)
#
#     return logger  # 日志记录器



def mylog02():
    # 读配置文件
    logging.config.fileConfig('../script/log.conf')
    logger = logging.getLogger('配置文件')
    return logger



if __name__ == "__main__":
    logger = mylog02()
    logger.info('通过配置文件生成的日志')