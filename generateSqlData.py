#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 14:16 
# @Author  : Zhangyp
# @File    : generateSqlData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""生成sql操作相关数据"""

from faker import Faker
from config import cfg
from datetime import datetime
from common.utils import ger_dates
from common.generator import PersonInfo, HospitalData

fake = Faker('zh_CN')

# 获取插入表
tables = cfg.get_raw('database', 'tableList')

# 时间分配开关
if_average_by_Time = cfg.get_bool('task', 'ifAverageByTime')

# 获取机构信息
organizationID = cfg.get('business', 'organizationID')
organizationName = cfg.get('business', 'organizationName')


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
def field_value(num, time=None):
    if if_average_by_Time:  # 判断是否生成平均的时间字段
        time_field = time  # 通过参数从平均分布时间的list里面获取
    else:  # 否则通过fake函数随机生成
        time_field = str(fake.date_between_dates(datetime.strptime(cfg.get('task', 'startDate'), "%Y-%m-%d"),
                                                 datetime.strptime(cfg.get('task', 'endDate'), "%Y-%m-%d"))),
    #     字段赋值
    pi = PersonInfo()
    hs = HospitalData(organizationName, organizationID, num)

    #     字段赋值
    kv = {"ExamUID": hs.examUid,
          "PatientID": time + '-' + str(num),
          "PIDAssigningAuthority": hs.assigningAuthority,
          "PatientMasterID": hs.pid,
          "PatientClass": hs.patientClass,
          "VisitUID": hs.visitUid,
          "OrganizationID": hs.hospitalCode,
          "FillerOrderNO": hs.fillerOrderNo,
          "FillerAssigningAuthority": hs.assigningAuthority,
          "FillerPatientID": time + '-' + str(num),
          "AccessionNumber": time.replace('-','')+str(num),
          "ServiceText": hs.examBodyPart,
          "ServiceSectID": hs.serviceSectId,
          "ProcedureName": hs.procedureName,
          "ProviderName": PersonInfo().name,
          "RequestDeptName": '申请科室',
          "RequestOrgName": hs.hospital,
          "RequestedDate": time + " 07:00:00",
          "ClinicDiagnosis": "临床诊断",
          "RegTime": time + " 08:00:00",
          "RegisterName": PersonInfo().name,
          "ExamDate": time + " 08:20:00",
          "ExamEndDate": time + " 08:25:00",
          "ExamLocation": hs.serviceSectId + '机房',
          "StudyInstanceUID": hs.studyUid,
          "ResultAssistantName": PersonInfo().name,
          # "ResultPrincipalID": "admin",
          "ResultPrincipalName": PersonInfo().name,
          "PreliminaryDate": time + " 14:07:05",
          "AuditDate": time + " 15:28:31",
          "ResultDate": time + " 15:28:31",
          "ResultServiceCenterUID": "00000000-0000-0000-0000-000000000000",
          "ResultStatus": "审核完成",
          "ResultStatusCode": "3080",
          "ResultPrintCount": 0,
          "AbnormalFlags": "阴性",
          "PrivacyLevel": 0,
          "PaymentsFlag": "1",
          "FilmCount": 0,
          "FilmNeed": "0",
          "HasImage": "1",
          "ImageLocation": 1,
          "ConsultStatus": 0,
          "LastUpdateDate": time + " 11:23:21.793",
          "DataSource": hs.examSystem,
          "LockFlag": "0",
          "LockUserUID": "00000000-0000-0000-0000-000000000000",
          "InWritingUserUID": "00000000-0000-0000-0000-000000000000",
          "MessageCount": 0,
          "UnProcessWorkflowCount": 0,
          "PushState": "0",
          "DeleteFlag": "0",
          "ResultSelfPrintCount": 0,
          "DrugDose": 0,
          "IdcasState": 0,
          "PriorityFlag": 0,
          "DigitalImageNeed": 0,
          "BusinessStatus": 2,
          "UploadFlag": "0",
          "ConsultationState": 2,
          "HasReport": 0,
          "RegisterFlag": "0",
          "IsInterconnectData": "0",
          "PushFlag": "0",

          "ImagingFinding": "*****对称，**居中，**未见明显病灶。",
          "ImagingDiagnosis": "**未见明显异常。",
          "UploadRetryTimes": 0,

          "IsMPI": 1,
          "CreateDate": time + " 11:22:09.027",
          "CreateOrgnizationID": hs.hospitalCode,
          "Name": pi.name,
          "Sex": pi.sex,
          "BirthDate": pi.birthday,
          "IDCardNO": pi.IDCard,
          "ContactPhoneNO": pi.phone_number,
          "Status": "0",

          "VisitID": "69915361-2e2b-4932-bf52-44e9a458d1f2",
          "PatientType": hs.patientClass,
          # "MedRecNO": "201809300013",
          "Age": pi.age,
          "AgeUnit": "岁",
          "PregnancyFlag": "0",
          "AdmitDate": time + " 07:56:30",
          "ReAmissionFlag": "0",
          "AdmitDeptName": hs.patientClass,
          "DeptName": hs.patientClass,

          "FileUID": hs.fileUID,
          "BusinessID": hs.businessID,
          "BusinessType": "Exam",
          "BusinessTime": time + " 07:56:30",
          "ClassCode": "Exam",
          "TypeCode": "ExamImage",
          "MimeType": "DICOMDIR",
          "FileSHA": "1adb6bb40a16591e330127f0e7ee8d09d09af861",
          "FileSize": 3250694,
          "FileCreateTime": time + " 09:35:53.943",
          "CreateOrganizationID": hs.hospitalCode,
          "FolderFlag": "0",
          "LocalFileIsAlreadyDeleted": "0",

          "ServiceUID": "88760571-e9e2-4536-9a6d-acaa012c9d83",
          "MediaUID": "5de204a7-4c32-416a-99e3-acaa012c8933",
          "FileRelativePath": "year\\month\\day\\Exam\\FileUID\\Exam\\ExamImage\\DICOMDIR",
          "CreateTime": time + " 09:35:53.95",
          "MigrationFlag": "0",
          "FileDeleteFlag": "0",
          "FileUploadFlag": "0",
          "ArchiveFlag": "0",
          "ArchiveRetryTimes": 0,
          "PushRetryTimes": 0
          }
    return kv


# 拼接sql语句
def generate_sql():
    # 获取插入的表list
    table_names = tables.split(',')
    insert_sql_list = []
    for table in table_names:
        # 获取插入的字段名
        filed_name = cfg.get_raw('database', table)
        # 去掉读取配置中出现的换行符
        if "\n" in filed_name:
            filed_name = filed_name.replace("\n", "")
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
        kv = field_value(i)  # 放在循环外面，使得有关联的字段值在每个表中生成的value一样
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
    begin_time = datetime.now()
    for i in range(num):  # 生成几组数据
        kv = field_value(i, date_list[i])  # 放在循环外面，使得有关联的字段值在每个表中生成的value一样
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
            # print('生成表{}数据完成,耗时:{}'.format(table, (datetime.now() - begin_time)))
        data_group.append(data_set)
        print('第{}组数据已生成'.format(str(i + 1)))
    # 做行列转化，使得每个表的values值在同1个list里面
    table_group = list(map(list, zip(*data_group)))
    print('{}组数据全部生成,耗时：{}'.format(str(num), datetime.now() - begin_time))
    return table_group


if __name__ == '__main__':
    # print(insert_values1(10))
    # l1 = insert_values(3)
    # for ii in l1:
    #     print(ii)
    generate_values_average_time(10000)
    # print(generate_sql())
