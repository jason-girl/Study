# _*_ coding:utf-8 _*_
# File Name: test02_logger
# Author： Emily
# Date:  2021/3/18  17:26
# Description : 封装日志


# 导包
import logging.handlers


def get_logger():
    # 获取 日志器
    logger = logging.getLogger()
    # 设置日志器级别
    logger.setLevel(logging.INFO)
    # 获取处理器 控制台
    sh = logging.StreamHandler()
    # 获取处理器 文件-以时间间隔
    th = logging.handlers.TimedRotatingFileHandler(filename="../log/log1.log",
                                               when='midnight', interval=1,
                                               backupCount=30, encoding="utf-8")
    # 设置格式器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(funcName)s:%(lineno)d] - %(message)s"
    fm = logging.Formatter(fmt)
    # 将格式器添加到 处理器 控制台
    sh.setFormatter(fm)
    # 将格式器添加到 处理器 文件
    th.setFormatter(fm)
    # 将处理器添加到 日志器
    logger.addHandler(sh)
    logger.addHandler(th)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info("信息被执行")
