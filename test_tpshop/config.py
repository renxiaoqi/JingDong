import os
from logging.handlers import TimedRotatingFileHandler

BASE_CA = os.path.dirname(os.path.abspath(__file__))
print(BASE_CA)
import logging
def init_logging():
    # 创建日志器
    my_logger= logging.getLogger()
    # 设置输出格式为info
    my_logger.setLevel(logging.INFO)
    # 创建处理器
    processor1 = logging.StreamHandler() # 输出到控制台
    # 输出到时分秒文件
    processor2 = TimedRotatingFileHandler("./log/time.log",when="d",interval=20,backupCount=0)
    # 输出到普通文件
    processor3 = logging.FileHandler("./log/putong.log")
    # 创建格式化器
    fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
    fmter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中
    processor1.setFormatter(fmter)
    processor2.setFormatter(fmter)
    processor3.setFormatter(fmter)

    # 将处理器添加到日志器中
    my_logger.addHandler(processor1)
    my_logger.addHandler(processor2)
    my_logger.addHandler(processor3)