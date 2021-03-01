# _*_ coding:utf-8 _*_
# File Name: test06
# Author： Emily
# Date:  2021/2/25  16:58
# Description : 操作浏览器的常用方法


from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# 打开URL
url = 'https://www.baidu.com/'
driver.get(url)
# 将浏览器 最大化
driver.maximize_window()
# 暂停2秒
sleep(2)
# 设置固定大小 300,200
driver.set_window_size(300, 200)
# 暂停2秒
sleep(2)
# 移动浏览器窗口位置 x: 320，y:150
driver.set_window_position(320, 150)
# 暂停2秒
sleep(2)
# 最大化
driver.maximize_window()
# 暂停2秒
sleep(2)
# 执行后退
driver.back()
# 暂停2秒
sleep(2)
# 执行前进
driver.forward()
# 暂停2秒
sleep(2)
# 输入搜索内容
driver.find_element_by_css_selector("#kw").send_keys('123')
# 暂停2秒
sleep(2)
# 刷新页面 目的：清空输入内容
driver.refresh()
# 暂停2秒
sleep(2)
# 获取页面title
title = driver.title
print('当前页面title', title)
# 获取当前页面URL
url = driver.current_url
print('当前页面URL', url)
# 退出浏览器驱动
driver.quit()
