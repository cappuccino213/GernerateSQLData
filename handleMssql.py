#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:24 
# @Author  : Zhangyp
# @File    : handleMssql.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from config import cfg
# from common.setLogger import set_logger
import pymssql


class MsSql:
    def __init__(self):
        self.conn = pymssql.connect(host=cfg.get('mssql_connect', 'host'),
                                    user=cfg.get('mssql_connect', 'user'),
                                    password=cfg.get('mssql_connect', 'pwd'),
                                    database=cfg.get('mssql_connect', 'db'),
                                    charset=cfg.get('mssql_connect', 'charset'))

        self.cur = self.conn.cursor()

    def query_sql(self, sql, args=None, is_all=False):
        """
        sql语句查询
        :param sql:查询的sql语句
        :param args:
        :param is_all:是否查询所有
        :return:
        """
        self.cur.execute(sql, args)
        if is_all:
            return self.cur.fetchall()
        else:
            return self.cur.fetchone()

    def cud_sql(self, sql, value, is_batch=False):
        """
        增删改
        :param sql:
        :param value:如果是批量insert，则value为list
        :param is_batch:是否批量操作，只用于insert
        :return:
        """
        if is_batch:
            try:
                self.cur.executemany(sql, value)
            except Exception as e:
                print("执行{0}{1}异常，异常{2}，操作回滚".format(sql, value, str(e)))
            else:
                self.conn.commit()
                # logger.info("事务提交成功")
                print("{} 事务提交成功".format(sql))
        else:
            try:
                self.cur.execute(sql, value)
            except Exception as e:
                print("执行{0}{1}异常，异常{2}，操作回滚".format(sql, value, str(e)))
            else:
                self.conn.commit()
                print("{} 事务提交成功".format(sql))

    def close_mssql(self):
        self.cur.close()
        self.conn.close()


# def handle_insert_sql(insert_sql):
#     """
#     处理insert语句，只要给出insert tableName (filed1,filed2...),后面的value会自动拼接
#     :param insert_sql:
#     :return:
#     """
#     count_field = insert_sql.count(',') + 1
#     values_exp = ','.join(['%s' for _ in range(count_field)])
#     insert_sql = "{0} values ({1})".format(insert_sql, values_exp)
#     return insert_sql


if __name__ == "__main__":
    db = MsSql()
    values = [('C', '测试机构1', '123', '', '', '', '', '', '', '', '-1', '00000000-0000-0000-0000-000000000000', '', '', 0,
               '', '', '', '', 0, 0, '', '', '', ''),
              ('E', '测试机构2', '123', '', '', '', '', '', '', '', '-1', '00000000-0000-0000-0000-000000000000', '', '', 0,
               '', '', '', '', 0, 0, '', '', '', '')]
    #     values=('D', '测试机构', '123', '', '', '', '', '', '', '', '-1', '00000000-0000-0000-0000-000000000000', '', '', 0, '', '', '', '', 0, 0, '', '', '', '')

    sql = "select * from OrganizationMst"
    sql1 = "INSERT INTO OrganizationMst (OrganizationID, OrganizationName, Alias, InputCode, ContactUserName, OfficePhoneNO, PersonalPhoneNO, Email, Address, OrganizationTypeCode, ParentOrganizationID, CreateUserUID, CreateDate, Memo, DeleteFlag, OrganizationCode, Province, City, District, SortNO, BusinessStatus, CardBackgroundColour, DefaultShareDuration, BackGroundURL, LogoURL)"
    sql_statement = handle_insert_sql(sql1)
    db.cud_sql(sql_statement, values, True)
    db.close_mssql()
