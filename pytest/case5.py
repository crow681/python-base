#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 11:38
# @Author  : wangjun
# @File    : case5.py
# @explain : 自动执行

import pytest

# @pytest.fixture(autouse=True)
# def get_session():
#     return print('获取session')
#
# def test_func():
#     """不使用固件"""
#     assert 1+1 == 2

@pytest.fixture(name='myname')
def myfuc_001_name():
    return 5

def test_myfuc(myname):
    assert myname == 5