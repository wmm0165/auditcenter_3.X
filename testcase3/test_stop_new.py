# -*- coding: utf-8 -*-
# @Time : 2019/7/29 14:01
# @Author : wangmengmeng

import unittest
import warnings
import time
from common.ipt import Ipt


class TestStop(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.ipt = Ipt()

    def test_01(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱未审核，则旧任务撤销重新产生任务--ok'''

        self.ipt.send.send('ipt_stop', '医嘱一', 1)
        self.assertIsNotNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        self.ipt.send.send('ipt_stop', '1', 1)  # 修改医嘱，失效时间大于等于当前时间
        self.assertIsNotNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        engineid = self.ipt.get_engineid(1)
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][0]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tsb1}}']))
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][1]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tsb1}}']))

    def test_02(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱未审核，则旧任务撤销重新产生任务--ok'''

        self.ipt.send.send('ipt_stop', '医嘱一', 1)
        self.assertIsNotNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        self.ipt.send.send('ipt_stop', '2', 1)  # 修改医嘱，失效时间小于当前时间
        engineid = self.ipt.get_engineid(1)
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][0]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tf1}}']))
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][1]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tf1}}']))

    def test_03(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱已审核，则不产生任务--nok（目前产生任务了）
        旧医嘱在有效期内（失效时间大于等于当前时间）'''
        self.ipt.send.send('ipt_stop', '医嘱一', 1)
        self.assertIsNotNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        engineid = self.ipt.get_engineid(1)
        self.ipt.ipt_audit(self.ipt.send.change_data['{{gp}}'], engineid, 0)
        self.ipt.send.send('ipt_stop', '1', 1)
        self.assertIsNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        self.ipt.send.send('ipt_stop', '医嘱二', 1)
        engineid2 = self.ipt.get_engineid(1)
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][0]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tsb1}}']))
        self.assertEqual(
            (self.ipt.orderList(engineid, 1))['data'][self.ipt.send.change_data['{{gp}}']][1]['orderInvalidTime'],
            int(self.ipt.send.change_data['{{tsb1}}']))

    def test_04(self):
        '''非新开具医嘱，stop_flag = 0,只修改失效时间且原医嘱已审核，则不产生任务-待测试
        旧医嘱不在有效期内（失效时间小于当前时间）'''
        self.ipt.send.send('ipt_stop', '3', 1)
        self.assertIsNotNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
        engineid = self.ipt.get_engineid(1)
        self.ipt.ipt_audit(self.ipt.send.change_data['{{gp}}'], engineid, 0)
        self.ipt.send.send('ipt_stop', '2', 1)  # 这里没有产生任务
        self.assertIsNone((self.ipt.selNotAuditIptList())['data']['engineInfos'])
