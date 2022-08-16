#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 14:26
# @Author  : wangjun
# @File    : case3.py
# @explain :
"""
固件使用范围作用域：
在首次请求时创建，根据scope参数声明，可选参数有:
function: 默认范围，在测试结束后自动销毁
class：在测试类中执行一次，每个方法都可用
module：每个模块执行一次，模块中的函数和方法都可用
package:每个包中执行一次，包中的模块都可以
session:一次测试只执行一次
"""

# 夹具执行顺序
import pytest

@pytest.fixture(scope='session')
def order():
    return []

@pytest.fixture
def func(order):
    order.append('function')

@pytest.fixture(scope='class')
def cla(order):
    order.append('class')

@pytest.fixture(scope='module')
def mod(order):
    order.append('module')

@pytest.fixture(scope='package')
def pack(order):
    order.append('package')

@pytest.fixture(scope='session')
def sess(order):
    order.append('session')

class TestClass:
    def test_order(self, func, cla, mod, pack, sess, order):
        assert order == ['session', 'package', 'module', 'function', 'class']


