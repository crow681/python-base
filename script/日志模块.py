#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 15:17
# @Author  : wangjun
# @File    : 日志模块.py

import logging
from logging import config
import yaml
def logmain():

    # 记录日志到文件
    logger = logging.getLogger('基本配置')
    logging.basicConfig(
        filename='../script/log.log',   # 保存到文件
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s-%(levelname)s-%(name)s-%(message)s',  # 格式化输出内容
        datefmt='%Y-%m-%d %H:%M:%S'


    )
    return logger

def mylog():
    """
    日志提供四类组件：记录器（Logger）、处理器(Handler)、过滤器(Filter)和格式器(formatter)
    自定义组件输出日志
    :return:
    """
    # 创建自定义的记录器
    logger = logging.getLogger('设置了组件的日志')
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

    return logger   # 日志记录器

def conflog():
    """
    基于配置文件配置的日志
    :return:
    """
    with open('../script/log_conf.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # print(conf)

    # 从yaml文件获取日志记录配置
    logging.config.dictConfig(data['logconf'])
    logger = logging.getLogger('myconf')

    return logger

if __name__ == "__main__":
    # 方式一：直接使用基础配置logging.basicConfig
    #  l = logmain()
    #  l.info('basicConfig模块配置')

    # 方式二： 自定义创建记录器
    # s = mylog()
    # s.info('显示创建记录器、处理器、格式器')

    # 方式三： 通过配置文件读取配置信息
     cn = conflog()
     cn.info('使用yaml创建配置字典')

