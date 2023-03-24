#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 14:54
# @Author  : wangjun
# @File    : test.py
# @explain :
import sys
import getopt


def myfunc1(a, b, c):
    print('第一个参数：'+a)
    print('第二个参数：'+b)
    print('第三个参数：'+c)


if __name__ == "__main__":
    #
    # argv = sys.argv[1:]
    # myfunc1(a=argv[0], b=argv[1], c=argv[2])
    args = '-a -b -cfoo oo g h'.split()

    optlist, arg = getopt.getopt(args, 'a:b:c:', ['-o'])
    print(optlist)
    print(arg)

