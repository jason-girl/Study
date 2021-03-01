# _*_ coding:utf-8 _*_
# File Name: day01
# Author： Emily
# Date:  2021/2/1  10:06
# Description : 进入百度首页


from selenium import webdriver
from time import sleep

# 获取浏览器
driver = webdriver.Chrome()
# 打开URL
driver.get("http://www.baidu.com")
# 暂停三秒
sleep(3)
# 关闭浏览器驱动
driver.quit()