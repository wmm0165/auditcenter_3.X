# -*- coding: utf-8 -*-
# @Time : 2019/10/29 14:38
# @Author : wangmengmeng
from common.send_data_new import send

class Audit721:
    """AUDIT-721 门诊处方开具时间小于处方明细的开始时间导致系统异常"""
    def test_recipe_small(self):
        """recipe_time<start_time"""
        send.send('opt,','audit721_1',1)

    def test_recipe_large(self):
        """recipe_time>start_time"""
        send.send('opt,', 'audit721_2', 1)

    def test_recipe_equal(self):
        """recipe_time=start_time"""
        send.send('opt,', 'audit721_3', 1)


if __name__ == '__main__':
    pass




