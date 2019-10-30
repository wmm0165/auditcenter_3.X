# -*- coding: utf-8 -*-
# @Time : 2019/10/29 14:38
# @Author : wangmengmeng
import os, sys
import pytest
sys.path.append(os.getcwd())


class TestOpt:
    """AUDIT-721 门诊处方开具时间小于处方明细的开始时间导致系统异常 < > ="""

    @pytest.mark.parametrize('xml_name', ['audit721_1', 'audit721_2', 'audit721_3'])
    def test_recipe_small(self, audit721_opt, xml_name):
        """recipe_time<start_time,产生待审任务"""
        audit721_opt.send.send('opt', 'audit721_1', 1)
        assert not (audit721_opt.selNotAuditOptList(1))['data']['optRecipeList']


class TestIpt:
    """住院医嘱开具时间与医嘱生效时间的关系测试"""

    @pytest.mark.parametrize('xml_name', ['audit721_4', 'audit721_5', 'audit721_6'])
    def test_order_small(self, audit721_ipt, xml_name):
        """order_time<order_valid_time,产生待审任务"""
        audit721_ipt.ipt.send('ipt', xml_name, 1)
        assert not (audit721_ipt.selNotAuditIptList())['data']['engineInfos']


if __name__ == '__main__':
    pass
