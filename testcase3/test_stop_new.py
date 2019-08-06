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

        self.ipt.send.send('ipt','医嘱一',1)
        engineid = self.ipt.get_engineid(1)
        self.ipt.send.send('ipt_stop', '医嘱一', 1)
        res = self.ipt.selNotAuditIptList()









