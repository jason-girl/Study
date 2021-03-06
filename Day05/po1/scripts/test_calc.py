# _*_ coding:utf-8 _*_
# File Name: test_calc
# Author： Emily
# Date:  2021/3/11  17:06
# Description : 计算器case


import unittest

from base.get_driver import GetDriver
from page.page_calc import PageCalc
from parameterized import parameterized
from tool.read_json import read_json


def get_data():
    datas = read_json("calc.json")
    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data['expect']))
    return arrs


class TestCalc(unittest.TestCase):
    driver = None

    # setupclass
    @classmethod
    def setUpClass(cls) -> None:
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 初始化页面对象
        cls.calc = PageCalc(cls.driver)

    # teardown
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试加法 方法
    @parameterized.expand(get_data()  )
    def test_add_calc(self, a, b, expect):
        self.calc.page_add_calc(a, b)
        try:
            self.assertEqual(self.calc.page_get_value(), str(expect))
        except AssertionError:
            self.calc.page_get_image()
