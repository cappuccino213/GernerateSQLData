#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 14:16 
# @Author  : Zhangyp
# @File    : generateSqlData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com


import random

import uuid
from faker import Faker
from config import cfg
from datetime import datetime
from common.utils import ger_dates

fake = Faker('zh_CN')

# 获取插入表
tables = cfg.get_raw('database', 'tableList')

# 时间分配开关
if_average_by_Time = cfg.get_bool('task', 'ifAverageByTime')


# 将生成数据赋值给字段
# def field_value():
#     kv = {"A_uid": uuid.uuid4(),
#           "A_uid2": uuid.uuid4(),
#           "A_field1": fake.name(),
#           "A_field2": random.choice(['男', '女']),
#           "A_field3": fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=120),
#           "Time": fake.date_between_dates(datetime.strptime(cfg.get('task', 'startDate'), "%Y-%m-%d"),
#                                           datetime.strptime(cfg.get('task', 'endDate'), "%Y-%m-%d")),
#           "B_uid": uuid.uuid4(),
#           "B_field1": fake.job(),
#           "B_field2": fake.address(),
#           "C_field1": fake.phone_number(),
#           "C_field2": str(random.randint(100, 300))}
#     return kv

# 将生成数据赋值给字段
def field_value(time=None):
    if if_average_by_Time:  # 判断是否生成平均的时间字段
        time_field = time  # 通过参数从平均分布时间的list里面获取
    else:  # 否则通过fake函数随机生成
        time_field = str(fake.date_between_dates(datetime.strptime(cfg.get('task', 'startDate'), "%Y-%m-%d"),
                                                 datetime.strptime(cfg.get('task', 'endDate'), "%Y-%m-%d"))),
    kv = {"A_uid": uuid.uuid4(),
          "A_uid2": uuid.uuid4(),
          "A_field1": fake.name(),
          "A_field2": random.choice(['男', '女']),
          "A_field3": fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=120),
          "Time": time_field,
          "B_uid": uuid.uuid4(),
          "B_field1": fake.job(),
          "B_field2": fake.address(),
          "C_field1": fake.phone_number(),
          "C_field2": str(random.randint(100, 300))}
    return kv


# 拼接sql语句
def generate_sql():
    # 获取插入的表list
    table_names = tables.split(',')
    insert_sql_list = []
    for table in table_names:
        # 获取插入的字段名
        filed_name = cfg.get_raw('database', table)
        # 拼接插入语句
        insert_part = "INSERT INTO {} ({})".format(table, filed_name)
        # 拼接赋值语句
        filed_num = len(filed_name.split(','))
        placeholder = ','.join(['%s' for _ in range(filed_num)])
        value_part = "VALUES ({})".format(placeholder)
        print('表{}的insert语句已生成'.format(table))
        insert_sql_list.append(insert_part + ' ' + value_part)
    return insert_sql_list


# 生成待插入的数据，随机时间
def generate_values(num):
    """
    :param num: 生成的values数量
    :return:
    """
    data_group = []  # 按表名分组
    for i in range(num):  # 生成几组数据
        kv = field_value()  # 放在循环外面，使得有关联的字段值在每个表中生成的value一样
        data_set = []
        for table in tables.split(','):  # 从配置文件获取表名的list
            filed_list = cfg.get_raw('database', table).split(',')
            values_list = []
            for filed in filed_list:
                if filed in kv.keys():
                    values_list.append(kv[filed])
                else:
                    values_list.append('')
            data_set.append(tuple(values_list))
        data_group.append(data_set)
        # print('第{}组数据已生成'.format(str(i + 1)))
    # 做行列转化，使得每个表的values值在同1个list里面
    table_group = list(map(list, zip(*data_group)))
    print('{}组数据全部生成'.format(str(num)))
    return table_group


# 生成待插入的数据，平均分布时间
def generate_values_average_time(num):
    """
    :param num: 生成的values数量
    :return:
    """
    data_group = []  # 按表名分组
    date_list = ger_dates(num, cfg.get('task', 'startDate'), cfg.get('task', 'endDate'))
    for i in range(num):  # 生成几组数据
        kv = field_value(date_list[i])  # 放在循环外面，使得有关联的字段值在每个表中生成的value一样
        data_set = []
        for table in tables.split(','):  # 从配置文件获取表名的list
            filed_list = cfg.get_raw('database', table).split(',')
            values_list = []
            for filed in filed_list:
                if filed in kv.keys():
                    values_list.append(kv[filed])
                else:
                    values_list.append('')
            data_set.append(tuple(values_list))
        data_group.append(data_set)
        # print('第{}组数据已生成'.format(str(i + 1)))
    # 做行列转化，使得每个表的values值在同1个list里面
    table_group = list(map(list, zip(*data_group)))
    print('{}组数据全部生成'.format(str(num)))
    return table_group


if __name__ == '__main__':
    # print(insert_values1(10))
    # l1 = insert_values(3)
    # for ii in l1:
    #     print(ii)
    print(generate_values(10))
