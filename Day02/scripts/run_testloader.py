# _*_ coding:utf-8 _*_
# File Name: run_testloader
# Author： Emily
# Date:  2021/3/2  18:14
# Description : 演示TestLoader()类的用法


import unittest

# 调用方法
suite = unittest.TestLoader().discover("../cases", 'test*.py')
# 执行 套件 方法
unittest.TextTestRunner().run(suite)
