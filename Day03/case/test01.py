# _*_ coding:utf-8 _*_
# File Name: test01
# Author： Emily
# Date:  2021/3/8  16:07
# Description :


import unittest


class Test01(unittest.TestCase):
    def test001(self):
        print("test001被执行")

    def test002(self):
        print("test002被执行")

    def test003(self):
        print("test003被执行")

    def test004(self):
        print("test004被执行")


if __name__ == '__main__':
    print("__name__的值：", __name__)
