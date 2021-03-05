# _*_ coding:utf-8 _*_
# File Name: test01_testcase
# Author： Emily
# Date:  2021/3/2  16:45
# Description : TestCase使用


# 导包
import unittest


# 编写求和函数
def add(x, y):
    return x+y


# 定义测试类并继承
class Test01(unittest.TestCase):
    # 定义测试方法 注意：以test字母开头
    def test_add01(self):
        # 调用要测的函数
        result = add(1, 1)
        print("结果为：", result)

    def test_add02(self):
        # 调用要测的函数
        result = add(1, 2)
        print("结果为：", result)

    def test_add03(self):
        # 调用要测的函数
        result = add(1, 3)
        print("结果为：", result)
