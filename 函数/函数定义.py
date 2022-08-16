#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 10:59
# @Author  : wangjun
# @File    : 函数定义.py
# @explain :

def ask_ok(name, ask='Are you ok?', answer='yes'):
    """默认值参数"""
    print(name, '说', ask, '回答', answer)


def cheesshop(kind, *args, **kwargs):
    """形参数"""
    print('你喜欢什么？', kind, end='\n')
    for arg in args:
        print(arg)
    for kw in kwargs:
        print(kw, ':', kwargs[kw])


if __name__ == "__main__":
    print('-------------默认参数、位置参数、关键字参数----------------')
    ask_ok('张三')
    ask_ok('张三', ask='吃了么？')
    ask_ok(name='张三', ask='早上好!', answer='早呀！')
    print('------------关键字参数----------------------')
    cheesshop('小明', ('苹果', '香蕉', '荔枝'))
    cheesshop('李明',{'水果': '凤梨', '食物': '鸡肉'})
    cheesshop('张飞', ('菠萝', '西瓜', '猕猴桃'), {'水果': '李子', '食物': '红烧肉'})