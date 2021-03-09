# _*_ coding:utf-8 _*_
# File Name: base
# Author： Emily
# Date:  2021/3/8  18:14
# Description :


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self):
        # self.driver = driver
        self.driver = webdriver.Chrome()
        # 打开url
        url = 'https://gssdev.haoshengy.com/pc_workbench/login'
        self.driver.get(url)
        # 最大化浏览器
        self.driver.maximize_window()

    # 查找元素方法(提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, num, timeout=30, poll=0.5):
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        return el[num]

    # 点击方法
    def base_click(self, loc, num):
        self.base_find_element(loc, num).click()

    # 输入方法
    def base_input(self, loc, num, value):
        el = self.base_find_element(loc, num)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc, num):
        return self.base_find_element(loc, num).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/fail.png")

    # 获取当前页面地址
    def base_get_current_url(self):
        return self.driver.current_url
