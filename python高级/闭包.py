# encoding:utf-8
"""
定义：在函数嵌套前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数的内部函数称为闭包。

"""


def out(name):
    def inner(school):

        print('他是{0}的{1}'.format(school, name))

    return inner  # inner函数就是闭包


f = out('小明')
f('浪洞小学')
