#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 15:32 
# @Author  : Zhangyp
# @File    : setLogger.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import logging
import logging.handlers

'''
日志模块
'''
LOG_FILENAME = 'gsd.log'
logger = logging.getLogger()


def set_logger():
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# print(LOG_FILENAME)