# _*_ coding:utf-8 _*_
# File Name: page_login
# Author： Emily
# Date:  2021/3/9  11:28
# Description :


# 用户名
import time

from selenium.webdriver.common.by import By

from Day04.base.base import Base

login_username = [(By.CLASS_NAME, 'el-input__inner'), 1]
login_password = [(By.CLASS_NAME, 'el-input__inner'), 2]
login_btn = [(By.CLASS_NAME, 'login__button'), 0]


class PageLogin(Base):

    def input_username(self, username):
        # 输入手机号
        self.base_input(login_username[0], login_username[1], username)

    def input_password(self, password):
        # 输入密码
        self.base_input(login_password[0], login_password[1], password)

    def click_login_button(self):
        # 点击登录
        self.base_click(login_btn[0], login_btn[1])

    def get_current_url(self):
        return self.base_get_current_url()

    # 截图
    def get_screenshot(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
        time.sleep(2)
        return self.get_current_url()
