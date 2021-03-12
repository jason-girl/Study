# _*_ coding:utf-8 _*_
# File Name: get_driver
# Author： Emily
# Date:  2021/3/11  17:20
# Description : 获取driver


from selenium import webdriver
from po1 import page


class GetDriver:
    # 设置类属性
    driver = None
    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
