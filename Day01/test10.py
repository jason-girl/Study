# _*_ coding:utf-8 _*_
# File Name: test10
# Author： Emily
# Date:  2021/3/1  16:52
# Description : 截图操作


# _*_ coding:utf-8 _*_
# File Name: test09
# Author： Emily
# Date:  2021/3/1  16:00
# Description : 切换多窗口操作


from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# 打开URL
url = 'https://www.baidu.com/'
driver.get(url)
# 将浏览器 最大化
driver.maximize_window()
# 输入搜索内容
driver.find_element_by_css_selector("#kw").send_keys('张杰')
# 点击 “百度一下”
driver.find_element_by_id("su").click()
sleep(2)
# 截图
driver.get_screenshot_as_file("../image/admin.png")
# 暂停2秒
sleep(2)
# 退出浏览器驱动
driver.quit()
