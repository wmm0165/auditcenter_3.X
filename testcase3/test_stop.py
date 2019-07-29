# -*- coding: utf-8 -*-
# @Time : 2019/7/29 14:01
# @Author : wangmengmeng
from common.template import Template
from config.read_config import ReadConfig
import unittest
import warnings
import time

class TestStop(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.tem = Template()

    def test_01(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱未审核，则旧任务撤销重新产生任务--ok'''

        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        self.tem.send_data('ipt_stop', '1', **self.tem.change_data)
        # print(engineid)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNotNone(res['data']['engineInfos'])

    def test_02(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱已审核，则不产生任务--nok（目前产生任务了）'''

        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        # print(engineid)
        ids = [engineid]
        self.tem.audit_multi(3, *ids)
        self.tem.send_data('ipt_stop', '1', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_03(self):
        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # print(engineid)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_04(self):
        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        # print(engineid)
        ids = [engineid]
        self.tem.ipt_audit(self.tem.change_data['{{gp}}'], engineid, 0)  # 审核打回任务
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_05(self):
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_11(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱未审核，则旧任务撤销重新产生任务--ok'''

        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        self.tem.send_data('ipt_stop', '1', **self.tem.change_data)
        # print(engineid)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNotNone(res['data']['engineInfos'])

    def test_12(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱已审核，则不产生任务--nok（目前产生任务了）'''

        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        # print(engineid)
        ids = [engineid]
        self.tem.audit_multi(3, *ids)
        self.tem.send_data('ipt_stop', '1', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_13(self):
        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # print(engineid)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_14(self):
        engineid = self.tem.get_ipt_engineid('ipt_stop', '医嘱一', 1)
        # print(engineid)
        ids = [engineid]
        self.tem.ipt_audit(self.tem.change_data['{{gp}}'], engineid, 0)  # 审核打回任务
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])

    def test_15(self):
        self.tem.send_data('ipt_stop', '2', **self.tem.change_data)
        # 查询待审列表
        time.sleep(3)
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '查询待审住院任务列表')
        param = {
            "patientId": self.tem.change_data['{{ts}}']
        }
        res = self.tem.post_json(url,param)
        print(type(res)) # 字典类型
        print(res)
        self.assertIsNone(res['data']['engineInfos'])







