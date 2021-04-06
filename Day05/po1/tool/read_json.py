# _*_ coding:utf-8 _*_
# File Name: read_json
# Author： Emily
# Date:  2021/3/15  16:04
# Description :


import json


def read_json(filename):
    filepath = "../data/" + filename
    # 调用 load 方法
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)


if __name__ == '__main__':
    datas = read_json("calc.json")
    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data['expect']))
    print(arrs)
