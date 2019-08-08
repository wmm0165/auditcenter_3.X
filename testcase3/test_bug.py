# -*- coding: utf-8 -*-
# @Time : 2019/8/8 17:39
# @Author : wangmengmeng
import unittest
import warnings
import time
from common.ipt import Ipt


class TestBug(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.ipt = Ipt()

    def test_01(self):
        """AUDIT-593"""
        self.ipt.send.send('ipt', 'test1', 1)
        self.ipt.send.send('ipt', 'test2', 1)


