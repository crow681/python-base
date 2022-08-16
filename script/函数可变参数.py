#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/29 9:47
# @Author  : wangjun
# @File    : 函数可变参数.py
# @explain :

def func01(*args):
    print(*args)


def func02(*args):

    print(args)



sqe = ('a','b')
func01(sqe)
func02(sqe)




