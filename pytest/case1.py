#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/18 17:33
# @Author  : wangjun
# @File    : case1.py
# @explain : pytest练习训练

import pytest

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c


def test_add():
    #  测试加法
    assert add(1, 1) == 3

@pytest.mark.slow
def test_sub():
    # 测试减法
    assert sub(8, 5) == 4


if __name__ == '__main__':
    pytest.main(['-x', 'case1'])
