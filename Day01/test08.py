# _*_ coding:utf-8 _*_
# File Name: test08
# Author： Emily
# Date:  2021/3/1  15:31
# Description : 滚动条操作


from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# 打开URL
url = 'https://www.baidu.com/'
driver.get(url)
# 将浏览器 最大化
driver.maximize_window()
# 输入搜索内容
driver.find_element_by_css_selector("#kw").send_keys('123')
# 点击 “百度一下”
driver.find_element_by_id("su").click()
# 暂停2秒
sleep(2)
# 滚动条拉到最后
js = "window.scrollTo(0, 10000)"
driver.execute_script(js)
# 暂停2秒
sleep(2)
# 退出浏览器驱动
driver.quit()
