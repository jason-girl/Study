# _*_ coding:utf-8 _*_
# File Name: test
# Author： Emily
# Date:  2021/2/3  14:33
# Description : 测试获取当前时间

import time
# now_time = datetime.datetime.now()
# yes_time = now_time + datetime.timedelta(days=-1)
# yes_time_nyr = yes_time.strftime('%Y-%m-%d') + 'T15:59:59.999Z'
# now_time_nyr = now_time.strftime('%Y-%m-%d') + 'T16:00:00.000Z'
# print(now_time_nyr)
import datetime

today = datetime.date.today()
today_time = int(time.mktime(today.timetuple())) * 1000
yes_time = today_time + 24*60*60*1000-1
print(yes_time)

