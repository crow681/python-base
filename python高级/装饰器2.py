# encoding:utf-8
"""
装饰带有返回值的函数

"""
def logging(fn):

    def inner(num1, num2):
        print('计算中……')
        res = fn(num1, num2)
        return res

    return inner

@logging
def sum_num(a, b):
    res = a + b
    return res

res = sum_num(2, 5)
print(res)
