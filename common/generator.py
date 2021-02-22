#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 13:54 
# @Author  : Zhangyp
# @File    : generator.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from faker import Faker
from random import choice, randint
import datetime
from uuid import uuid4
from pydicom.uid import generate_uid
from common.dataSource import exam_dict

"""数据生成器"""
fake = Faker('zh_CN')

"""个人信息数据"""


class PersonInfo:
    def __init__(self):
        self.sex = choice(['男', '女'])
        # self.name = self.name()
        self.name = fake.name()
        # self.name_spell = fake.name_spell()
        # self.sex = choice(['f', 'm'])
        self.birthday = self.birthday()
        self.age = datetime.date.today().year - self.birthday.year
        # self.address = fake.address()
        # self.company = fake.company()
        self.job = fake.job()
        self.IDCard = self.id_card()
        self.phone_number = fake.phone_number()

    # 根据性别随机姓名
    def name(self):
        if self.sex == '男':
            return fake.name_female()
        if self.sex == '女':
            return fake.name_male()

    @staticmethod
    def birthday():
        return fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=90)

    # @staticmethod
    def id_card(self):
        from common.dataSource import CODE_LIST
        region_code = choice(CODE_LIST)
        bird_code = self.birthday.strftime('%Y%m%d')
        sequence_code = str(randint(100, 300))
        # 前17位地区码+生日+3位顺序号
        _id = region_code + bird_code + sequence_code

        # 计算校验码
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        count = 0
        for i in range(0, len(_id)):
            count = count + int(_id[i]) * weight[i]
        _id = _id + checkcode[str(count % 11)]
        return _id


"""医院信息"""


class HospitalData:

    def __init__(self, hos_name, hos_code, increment_num):
        self.hospital = hos_name
        self.hospitalCode = hos_code
        # self.exam_system = choice(['RIS','PIS','ECG','UIS','XIS','LIS']) # 检查系统
        self.examSystem = choice(['RIS'])
        self.examUid = uuid4()
        self.pid = uuid4()
        self.visitUid = uuid4()
        self.patientClass = self.patient_class()
        self.serviceSectId = self.service_sect_id()
        self.assigningAuthority = '{}.{}.{}'.format(self.hospitalCode, self.examSystem, self.serviceSectId)
        self.accessionNo = increment_num
        self.fillerOrderNo = '{}.{}{}'.format(self.assigningAuthority, self.examSystem, self.accessionNo)
        self.examBodyPart = self.exam_body_part()
        self.procedureId = self.procedure_id()
        self.procedureName = self.procedure_name()
        self.studyUid = generate_uid()
        self.fileUID = uuid4()
        self.businessID = self.examUid

    def patient_class(self):
        if self.examSystem == 'RIS':
            return choice(['门诊', '住院', '急诊', '体检'])
            # return choice([1000, 2000, 3000, 4000])

    def service_sect_id(self):
        if self.examSystem == 'RIS':
            return choice(['CR', 'DR', 'CT', 'RF', 'XA', 'MR', 'MG'])
            # return exam_dict(self.serviceSectId).get('ServiceSectID')

    def procedure_id(self):
        if self.examSystem == 'RIS':
            return exam_dict(self.serviceSectId).get('ProcedureID')

    def procedure_name(self):
        if self.examSystem == 'RIS':
            return exam_dict(self.serviceSectId).get('ProcedureName')

    def exam_body_part(self):
        if self.examSystem == 'RIS':
            return exam_dict(self.serviceSectId).get('ExamBodyPart')


class File:
    pass


if __name__ == '__main__':
    for i in range(10):
        hp = HospitalData('测试医院', 'testcode', i)
        pi = PersonInfo()
        # print(hp.serviceSectId)
        print(type(pi.id_card()))
        # print(PersonInfo().name)
