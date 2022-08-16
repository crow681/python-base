#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 18:58
# @Author  : wangjun
# @File    : a1.py
# @explain :

def login(name, passwd):
    return len(name), len(passwd)

name , passwd = 'usero1', '123456'
user, psd = login(name, passwd)
print(user)
print(psd)