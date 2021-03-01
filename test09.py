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
# 获取当前窗口
current_handle = driver.current_window_handle
# 点击第一条搜索结果
sleep(1)
driver.find_element_by_css_selector('div>h3>a').click()
sleep(2)
# 获取所有窗口句柄
handles = driver.window_handles
# 判断不是当前窗口句柄
for h in handles:
    if h != current_handle:
        # 切换窗口
        driver.switch_to.window(h)
# 暂停2秒
sleep(2)
# 退出浏览器驱动
driver.quit()
