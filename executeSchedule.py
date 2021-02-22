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
from datetime import datetime
import threading

"""执行计划，主程序运行"""

data_size = cfg.get_int('task', 'dataAmount')


def insert(sql_statement, value):
    # begin_time = time.time()
    begin_time = datetime.now()
    db = MsSql()
    db.cud_sql(sql_statement, value, is_batch=True)
    db.close_mssql()
    print("插入sql语句耗时：{}".format(datetime.now() - begin_time))


def main():
    # 1生成sql语句
    # begin_time = time.time()
    begin_time = datetime.now()
    sql_statements = generate_sql()
    # sql_time = time.time()
    print("生成sql语句耗时：{}".format(datetime.now() - begin_time))
    # 2生成待插入数据
    if if_average_by_Time:  # 判断是否按平均分布时间生成
        values = generate_values_average_time(data_size)
    else:
        values = generate_values(data_size)
    # values_time = time.time()
    # print("生成数据耗时：{}".format(values_time - sql_time))
    # 3数据插入
    if cfg.get_bool('task', 'ifMultiThread'):  # 多线程插入，几个sql几个线程
        threads = [threading.Thread(target=insert, args=(sql_statements[i], values[i],)) for i in
                   range(len(sql_statements))]
        for thread in threads:
            thread.start()
    else:  # 按照sql list的顺序插入
        for i in range(len(sql_statements)):
            insert(sql_statements[i], values[i])
    # end_time = time.time()
    # print("插入数据耗时：{}".format(end_time - values_time))


if __name__ == '__main__':
    main()
