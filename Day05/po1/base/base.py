# _*_ coding:utf-8 _*_
# File Name: base
# Author： Emily
# Date:  2021/3/11  15:01
# Description :


from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 元素定位信息，格式为元组
        :param timeout: 默认超时时间30秒
        :param poll: 访问频率，默认0.5秒查找一次
        :return: 返回查找到的元素
        """
        # 显示等待
        ele = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
        return ele

    # 点击
    def base_click(self, loc):
        # 调用查找元素 并点击
        self.base_find_element(loc).click()

    # 获取value属性方法封装
    def base_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性
        return self.base_find_element(loc).get_attribute("value")

    # 截图
    def base_get_img(self):
        self.driver.get_screentshot_as_file("../image/fail.png")
