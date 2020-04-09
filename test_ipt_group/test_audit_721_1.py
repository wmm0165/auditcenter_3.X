# -*- coding: utf-8 -*-
# @Time : 2020/4/9 14:26
# @Author : wangmengmeng
import pytest
class TestIpt:
    """住院医嘱开具时间与医嘱生效时间的关系测试"""

    @pytest.mark.parametrize('xml_name', ['audit721_4', 'audit721_5', 'audit721_6'])
    def test_order_small(self, zy, xml_name):
        """order_time<order_valid_time,order_time>order_valid_time,order_time=order_valid_time均产生待审任务"""
        zy.send.send('ipt', xml_name, 1)
        assert (zy.selNotAuditIptList())['data']['engineInfos']