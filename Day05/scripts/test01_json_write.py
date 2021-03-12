# _*_ coding:utf-8 _*_
# File Name: test01_json_write
# Author： Emily
# Date:  2021/3/11  14:31
# Description : 写入json的例子


import json

# 定义写的内容
data = {"name": "李四", "age": "12"}
# 获取文件流 并 写入数据
with open("../data/write.json", "w", encoding="UTF-8")as f:
    json.dump(data, f, ensure_ascii=False)
