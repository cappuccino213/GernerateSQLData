#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 17:42 
# @Author  : Zhangyp
# @File    : executeSchedule.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from handleMssql import MsSql
from generateSqlData import generate_sql, generate_values, generate_values_average_time, if_average_by_Time
from config import cfg
import time
import threading

"""执行计划"""

data_size = cfg.get_int('task', 'dataAmount')


def insert_thread():
    db = MsSql()

    # 1生成sql语句
    begin_time = time.time()
    sql_statements = generate_sql()
    sql_time = time.time()
    print("生成sql语句耗时：{}".format(sql_time))

    # 2生成待插入数据
    # 判断是否按平均分布时间生成
    if if_average_by_Time:
        values = generate_values_average_time(data_size)
    else:
        values = generate_values(data_size)
    data_time = time.time()
    print("生成数据耗时：{}".format(data_time - sql_time))

    # 3数据插入
    for i in range(len(sql_statements)):
        db.cud_sql(sql_statements[i], values[i], is_batch=True)
    db.close_mssql()
    end_time = time.time()
    print("插入数据耗时：{}".format(end_time - data_time))
    print("总耗时:{}".format(end_time - begin_time))


def insert(sql_statement, value):
    db = MsSql()
    db.cud_sql(sql_statement, value, is_batch=True)
    db.close_mssql()


def main():
    # 1生成sql语句
    sql_statements = generate_sql()
    # 2生成待插入数据
    if if_average_by_Time:  # 判断是否按平均分布时间生成
        values = generate_values_average_time(data_size)
    else:
        values = generate_values(data_size)
    # 3数据插入
    if cfg.get_bool('task', 'ifMultiThread'):  # 多线程插入，几个sql几个线程
        threads = [threading.Thread(target=insert, args=(sql_statements[i], values[i],)) for i in
                   range(len(sql_statements))]
        for thread in threads:
            thread.start()
    else:  # 按照sql的顺序插入
        for i in range(len(sql_statements)):
            insert(sql_statements[i], values[i])


if __name__ == '__main__':
    main()
