# _*_ coding:utf-8 _*_
# File Name: test03_name_location
# Author： Emily
# Date:  2021/2/1  16:40
# Description : name定位案列


from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
url = 'http://confluence.huisaas.com/'
driver.get(url)
# 查找用户名元素,输入用户名
driver.find_element_by_name('os_username').send_keys('admin')
# 查找密码元素,输入密码
driver.find_element_by_name('os_password').send_keys('123456')
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
