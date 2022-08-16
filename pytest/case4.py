#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 18:08
# @Author  : wangjun
# @File    : case4.py
# @explain : 固件预处理
import pytest


@pytest.fixture()
def connect():
    print('数据库链接成功')
    yield
    print('数据库关闭成功！')


def select(id):
    d = {'001': '张三'}
    return d[id]


def test_select(connect):
    assert select(id='001') == '张三'


def login(name, passwd):
    return len(name), len(passwd)

@pytest.mark.parametrize('name, passwd', [('user01', '12345678'), ('user1', '12345678'), ('user001', '1234567')])
@pytest.mark.login
def test_login(name, passwd):
    user, psd = login(name, passwd)
    assert 6 <= user <= 10, '用户名长度需要为6到10位'
    assert 8 <= psd <= 12, '密码长度为8到12位'



