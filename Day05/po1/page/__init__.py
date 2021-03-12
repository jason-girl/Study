# _*_ coding:utf-8 _*_
# File Name: __init__.py
# Author： Emily
# Date:  2021/3/11  15:01
# Description : 计算器配置数据
from selenium.webdriver.common.by import By

url = "http://cal.apple886.com/"

# 由于数字键，有一定的规律， 所以暂时先不用定位此键
# calc_num = By.CSS_SELECTOR, "simple9"
# 加号
calc_add = By.CSS_SELECTOR, "#simpleAdd"
# 等号
calc_eq = By.CSS_SELECTOR, "#simpleEqual"
# 获取结果
calc_result = By.CSS_SELECTOR, "#resultIpt"
# 清屏
calc_clear = By.CSS_SELECTOR, "#simpleClearAllBtn"
