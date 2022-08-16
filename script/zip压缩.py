#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 10:25
# @Author  : wangjun
# @File    : zip压缩.py

import zipfile
import os

# abs_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.isfile(abs_path))
# file_path = abs_path


def zip(zippath, file_path):
    """

    :param zippath:压缩包名称路径
    :param file_path: 需要压缩的文件
    :return:
    """

    if os.path.isfile(file_path):
        with zipfile.ZipFile(zippath, 'w') as zf:
            zf.write(file_path)
    else:
        with zipfile.ZipFile(zippath, 'w') as zf:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path)

if __name__ == '__main__':

    zip(r'D:\github\测试报告.zip', r'D:\github\autotestpro\Report')







