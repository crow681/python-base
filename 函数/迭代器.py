#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 11:32
# @Author  : wangjun
# @File    : 迭代器.py
# @explain :

"""
迭代器：
一个表示数据流的对象；
每次只返回一个元素；
必须支持__next__()方法，并总是返回数据流下一个元素

内置的iter()函数接收任意对象并返回一个迭代器，如果对象不支持会返回TypeError异常
"""
with open(r'D:\Work_bmsoft\04积分平台项目Scurm\积分平台项目基础信息.txt', 'r', encoding='utf-8') as file:
    L = file.readlines()
    newlist = []
    for i in L:
        newlist.append(i.rstrip())
    print(newlist)


class Number:
    def __iter__(self):
