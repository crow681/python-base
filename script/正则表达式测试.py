#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/29 16:50
# @Author  : wangjun
# @File    : 正则表达式测试.py
# @explain :

import re


text = 'doing, doone'
pattern = r'o{2}'
res = re.findall(pattern, text)
print(res)