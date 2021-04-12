# _*_ coding:utf-8 _*_
# File Name: readexcel
# Author： Emily
# Date:  2021/4/9  18:05
# Description : 读取Excel中的数据


import openpyxl


# 读取excel数据的类
class ReadExcel(object):
    def __init__(self, file_name, sheet_name):
        """
        这个是用来初始化读取对象的
        :param file_name: 文件名 ---> str类型
        :param sheet_name: 表单名 ———> str类型
        """
        # 打开文件
        self.wb = openpyxl.load_workbook(file_name)
        # 选择表单
        self.sh = self.wb[sheet_name]

    def read_data_line(self):
        # 按行读取数据转化为列表
        rows_data = list(self.sh.rows)
        # 获取表单的表头信息
        titles = []
        for title in rows_data[0]:
            titles.append(title.value)
        # 定义一个空列表用来存储测试用例
        cases = []
        for case in rows_data[1:]:
            data = []
            # 获取一条测试用例数据
            for cell in case:
                data.append(cell.value)
                # 将该条数据存放至cases中 通过zip聚合打包用例的标题和数据
                case_data = dict(zip(titles, data))
                cases.append(case_data)
        return cases


if __name__ == '__main__':
    r = ReadExcel('cases.xlsx', 'test_case')
    data1 = r.read_data_line()
    print(data1)
