# _*_ coding:utf-8 _*_
# File Name: test04_class_name_location
# Author： Emily
# Date:  2021/2/1  17:02
# Description : class_name 定位案列


from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
url = 'http://confluence.huisaas.com/'
driver.get(url)
# 查找用户名元素,输入用户名
driver.find_element_by_class_name('text').send_keys('admin')
# 查找密码元素,输入密码
driver.find_element_by_class_name('password').send_keys('123456')
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
