# _*_ coding:utf-8 _*_
# File Name: page_calc
# Author： Emily
# Date:  2021/3/11  16:26
# Description : 计算器页面


from selenium.webdriver.common.by import By
from po1.base.base import Base
from po1 import page


class PageCalc(Base):
    # 点击数字方法
    def page_click_num(self, num):
        for n in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)

    # 点击加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_click_eq(self):
        self.base_click(page.calc_eq)

    # 获取结果方法
    def page_get_value(self):
        return self.base_get_value(page.calc_result)

    # 点击清屏
    def page_clear(self):
        self.base_get_img()

    # 截图
    def page_get_image(self):
        self.base_get_img()

    # 组装加法页方法
    def page_add_calc(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()
