# _*_ coding:utf-8 _*_
# File Name: test01_logger
# Author： Emily
# Date:  2021/3/18  16:41
# Description :


import logging.handlers

# 获取logger
logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.INFO)
# 获取控制台 处理器
sh = logging.StreamHandler()
# 到文件 根据时间切割
fh = logging.handlers.TimedRotatingFileHandler(filename="../log/logtime.log", when='S', interval=1, backupCount=3)
# 设置 处理器 级别 扩展 设置为error级别，只有error级别信息才会写入文件
fh.setLevel(logging.ERROR)
# 添加格式器
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(funcName)s:%(lineno)d] - %(message)s"
fm = logging.Formatter(fmt)
# 将格式器 添加到处理器中
sh.setFormatter(fm)
fh.setFormatter(fm)
# 将控制台处理器添加到logger
logger.addHandler(sh)
logger.addHandler(fh)
# 输入信息
logger.info("info")
logger.debug("debug")
logger.error("error")
logger.warning("warning")
