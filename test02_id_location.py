# _*_ coding:utf-8 _*_
# File Name: test02_id_location
# Author： Emily
# Date:  2021/2/1  14:27
# Description : id定位案列


from selenium import webdriver
from time import sleep

# 获取浏览器对象
driver = webdriver.Chrome()
# 打开URL
# 注意：\反斜杠在python中是转义字符 r:修饰的字符串，如果字符串中有转义字符，不进行转义使用
url = 'http://confluence.huisaas.com/'
driver.get(url)
# 查找用户名元素
username = driver.find_element_by_id('os_username')
# 查找密码元素
password = driver.find_element_by_id('os_password')
# 用户名输入
username.send_keys('admin')
# 密码输入
password.send_keys('123456')
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
