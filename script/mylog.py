#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 11:05
# @Author  : wangjun
# @File    : mylog.py
# @explain :

import logging
def main():
        """自定义日志配置"""
        logger = logging.getLogger('mylog') # 初始化记录器
        logging.basicConfig(
                filename='../script/log.log',   # 保存到文件
                encoding='utf-8',
                level=logging.INFO,
                format='%(asctime)s-%(levelname)s-%(name)s-%(message)s',  # 格式化输出内容
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        return logger

