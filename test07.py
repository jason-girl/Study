# _*_ coding:utf-8 _*_
# File Name: test07
# Author： Emily
# Date:  2021/2/26  14:03
# Description : 鼠标操作


from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开URL
url = 'https://haoshengy.com/pc_workbench/login'
driver.get(url)
# 将浏览器 最大化
driver.maximize_window()
# 实例化并获取 ActionChains类
action = ActionChains(driver)
# 定位用户名 在用户名上 右击鼠标 预期：粘贴
element = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
action.context_click(element[1]).perform()
# 暂停2秒
sleep(2)
# 输入用户名 admin 并双击 预期：选中admin
element[1].send_keys('admin')
action.double_click().perform()
# 暂停2秒
sleep(2)
# 退出浏览器驱动
driver.quit()
