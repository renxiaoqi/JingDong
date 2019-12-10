import logging
import time
from logging.handlers import TimedRotatingFileHandler


class init_logging(object):
    # 创建日志器
    my_logger = logging.getLogger()
    # 设置输出日志级别
    my_logger.setLevel(logging.INFO)
    # 创建处理器
    # 输出到控制台
    prcessager1 = logging.StreamHandler()
    # 生成时分秒日志文件
    prcessager2 = TimedRotatingFileHandler("./log/case{}.log".format(time.strftime("%H_%M_%S")),when="M",interval=5,backupCount=0)
    # 生成普通日志文件
    prcessager3 = logging.FileHandler("./loo.log")
    # 创建格式化器
    gsh = logging.Formatter(fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")
    # 将格式化器添加到处理器中
    prcessager1.setFormatter(gsh)
    prcessager2.setFormatter(gsh)
    prcessager3.setFormatter(gsh)
    # 将处理器添加到日志器中
    my_logger.addHandler(prcessager1)
    my_logger.addHandler(prcessager2)
    my_logger.addHandler(prcessager3)