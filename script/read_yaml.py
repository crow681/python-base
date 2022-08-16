#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 17:20
# @Author  : wangjun
# @File    : read_yaml.py

import yaml

with open('../my.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
    print(data['evn'])
    print(data['mail'])
    print('普通数据:{0}'.format(data['list1']))
    print('嵌套数组{0}'.format(data['list2']))

