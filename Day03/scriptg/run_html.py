# _*_ coding:utf-8 _*_
# File Name: run_html
# Author： Emily
# Date:  2021/3/8  15:44
# Description : 生成测试报告


import unittest
import time

from tools.HTMLTestRunner import HTMLTestRunner

# 定义 测试套件
suite = unittest.defaultTestLoader.discover("../case", pattern="test*.py")
# 定义报告存放路径及文件名称
report_dir = "../report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
# 获取报告文件流 并执行
with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f, verbosity=2, title="XXX自动化测试报告", description="操作系统")
