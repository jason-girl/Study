# _*_ coding:utf-8 _*_
# File Name: test03_fixture_function
# Author： Emily
# Date:  2021/3/3  18:04
# Description :  Fixture的用法


import unittest


class Test03(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass被执行")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass被执行")

    def setUp(self):
        print("setUp被执行")

    def tearDown(self):
        print("tearDown被执行")

    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")
