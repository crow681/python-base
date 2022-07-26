#  encoding:utf-8
"""
装饰器特点：
1.不修改已有函数的源代码
2.不修改已有函数的调用方式
3.给已有函数增加额外功能

装饰器其实就是一个闭包函数
语法：
def decorator(fn):  #fn:被装饰的函数
    def inner():
        '''执行函数之前‘’‘
        fn() # 执行被装饰的目标函数
        ’‘’执行函数之后‘’‘
    return inner
"""

def check(fn):  # 添加登录验证功能
    def inner():
        print("请先登录")
        fn()


    return inner

@check
def comment():
    print("发表评论")


# comment = check(comment)

comment()
