# _*_ coding:utf-8 _*_
# File Name: test11
# Author： Emily
# Date:  2021/3/1  17:35
# Description : 通过cookie 跳过登录

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# 打开URL
url = 'https://www.baidu.com/'
driver.get(url)
# 将浏览器 最大化
driver.maximize_window()
# 设置cookie
driver.add_cookie({"name": "BDUSS", "value": "根据实际情况填写"})
# 暂停2秒
sleep(2)
# 刷新
driver.refresh()
# 退出浏览器驱动
driver.quit()
