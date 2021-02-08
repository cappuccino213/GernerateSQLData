#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 13:47 
# @Author  : Zhangyp
# @File    : utils.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from datetime import datetime, timedelta

"""日期/时间相关"""


# 判断日期的合法性
def is_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False


# 计算两个日期相差天数
def date_diff(start_date, end_date):
    if is_date(start_date) and is_date(end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return (end - start).days


# 生成指定数量的日期列表
def ger_dates(amount, start_date, end_date):
    """
    :param amount: 总数
    :param start_date: 起始日期
    :param end_date: 结束日期
    :return: 返回日期列表，当amount<date_diff(start_date, end_date) + 1 时，会只生成end_date的数据
    """
    days = date_diff(start_date, end_date) + 1  # 生成的天数
    per_day_amount = amount // days  # 每天需要生成的数量，取整数
    begin_date = start_date  # 起始日期
    dates_list = []
    if amount % days == 0:  # 是否能出尽
        # 平均每天生成一组日期列表
        for day in range(days):
            dates = [begin_date for _ in range(per_day_amount)]
            begin_date = (datetime.strptime(begin_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            dates_list.extend(dates)
        return dates_list
    else:
        # 平均每天生成一组日期列表
        for day in range(days):
            if day == days - 1:
                per_day_amount += amount % days  # 最后一组加上余数
            dates = [begin_date for _ in range(per_day_amount)]
            begin_date = (datetime.strptime(begin_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            dates_list.extend(dates)
        return dates_list


if __name__ == "__main__":
    # print(is_date('2021-13-29'))
    # print(date_diff('2021-2-28', '2021-1-29'))
    print(ger_dates(4, '2021-02-28', '2021-03-02'))
