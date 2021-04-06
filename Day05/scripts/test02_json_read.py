# _*_ coding:utf-8 _*_
# File Name: test02_json_read
# Author： Emily
# Date:  2021/3/11  14:50
# Description : 读取json文件


import json

# 打开要读取的文件流 并调用load方法
with open("../data/write.json", encoding="utf-8")as f:
    print(json.load(f))
