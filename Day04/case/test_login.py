# _*_ coding:utf-8 _*_
# File Name: test_login
# Author： Emily
# Date:  2021/3/9  14:56
# Description :


import unittest
from Day04.page.page_login import PageLogin
from parameterized import parameterized


def get_data():
    return [("xxxxxxxxxxx", "12345678"), ("23647821046", "12345678"), ("95555555555", "11111111")]


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 实例化 获取页面对象 PageLogin
        self.login = PageLogin()

    def tearDown(self) -> None:
        # 关闭 driver驱动对象
        self.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, username, password):
        url1 = "https://gssdev.haoshengy.com/pc_workbench/workbench/overview"
        # 调用登录方法
        url2 = self.login.page_login(username, password)
        try:
            # 断言操作
            self.assertEqual(url1, url2)
        except AssertionError:
            # 截图
            self.login.get_screenshot()
