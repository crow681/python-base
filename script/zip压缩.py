#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 10:25
# @Author  : wangjun
# @File    : zip压缩.py

import zipfile
import os

<<<<<<< HEAD
def zip(zippath, file_path):
    """
=======
# abs_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.isfile(abs_path))
# file_path = abs_path


def zip(zippath, file_path):
    """

>>>>>>> 6575801c7251cb280fbdc6e05cc349ae6d2975ea
    :param zippath:压缩包名称路径
    :param file_path: 需要压缩的文件
    :return:
    """
<<<<<<< HEAD
    # 压缩文件或文件夹
=======

>>>>>>> 6575801c7251cb280fbdc6e05cc349ae6d2975ea
    if os.path.isfile(file_path):
        with zipfile.ZipFile(zippath, 'w') as zf:
            zf.write(file_path)
    else:
        with zipfile.ZipFile(zippath, 'w') as zf:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path)

<<<<<<< HEAD
def open(zipath, filepath):
    """

    :param zipath: 需要解压的文件
    :param filepath: 解压后文件保存路径
    :return:
    """
    with zipfile.ZipFile(zipath, 'r') as zf:
        zf.extractall(filepath)


if __name__ == '__main__':

    #zip(r'D:\github\测试报告.zip', r'D:\github\autotestpro\Report')
    open(r'D:\github\python-base\dict\测试报告.zip', r'D:\github\python-base\dict\测试报告')
=======
if __name__ == '__main__':

    zip(r'D:\github\测试报告.zip', r'D:\github\autotestpro\Report')

>>>>>>> 6575801c7251cb280fbdc6e05cc349ae6d2975ea






