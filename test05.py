# _*_ coding:utf-8 _*_
# File Name: test05
# Author： Emily
# Date:  2021/2/20  15:36
# Description : css选择器

"""
    方法：
        driver.find_element_by_css_selector()
        获取文本的方法 元素.text
"""


from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
# 打开URL
url = 'http://confluence.huisaas.com/'
driver.get(url)
# 1. 使用CSS id选择器 定位用户名 输入admin
driver.find_element_by_css_selector("#os_username").send_keys('admin')
sleep(1)
# 2. 使用CSS 属性选择 定位密码框 输入123456
driver.find_element_by_css_selector("[name = 'os_password']").send_keys('123456')
sleep(1)
# 3. 使用CSS class 选择器 定位用户名 输入admin
driver.find_element_by_css_selector(".text   ").clear()
sleep(1)
driver.find_element_by_css_selector(".text   ").send_keys('admin1')
# 4. 使用CSS 元素选择器 定位label标签获取文本值
label = driver.find_element_by_css_selector("label").text
print('获取的label标签的值：', label)
# 5. 使用CSS 层级选择器 定位密码框 输入22222222
driver.find_element_by_css_selector("fieldset>div>input[placeholder='密码']").clear()
sleep(1)
driver.find_element_by_css_selector("fieldset>div>input[placeholder='密码']").send_keys('22222222')
# 暂停3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
