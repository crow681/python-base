#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 15:38
# @Author  : wangjun
# @File    : 字典方法.py
# @explain :

def meth_items():
    """items()"""
    d = {'姓名': '张三', '学号': '001', '科目': '数学'}
    for k, v in d.items():
        print(k, ':', v)

