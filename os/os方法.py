#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 10:24
# @Author  : wangjun
# @File    : os方法.py
# @explain : os常用方法示例

import os, sys

#   返回当前工作路径
cwd = os.getcwd()
print(f'当前路径是{cwd}')
#  返回指定文件夹包含的文件或文件夹名字列表
listdir = os.listdir('../script')
print('指定路径下的文件列表：', listdir)
# 递归创建多层目录
path1 = '../os/wangjun/test/testcase/apicase'
path2 = '../os/wangjun/test/testcase/webcase'
if path1:
    print('已创建路径')
    pass
else:
    os.makedirs(path1)
if path2:
    print('已创建路径')
    pass
else:
    os.makedirs(path2)

# 创建文件目录
path3 = '../os/wangjun/report'
if path3:
    print('已创建文件路径')
    pass
else:
    os.mkdir()

# 打开文件
with open('../os/wangjun/test/testcase/apicase/接口测试用例.txt', 'r', encoding='utf-8') as file:
    #print(file.readline())
    print(file.read(4))
# 创建、删除文件

with open('../os/wangjun/test/testcase/webcase/file.txt', 'x') as file:
    file.write('aaa')
    print('已创建file文件')
os.remove('../os/wangjun/test/testcase/webcase/file.txt')
print('file删除成功')
