# -*- coding: utf-8 -*-
# @Time : 2020/4/9 14:28
# @Author : wangmengmeng
import pytest
class TestOpt:
    """AUDIT-721 门诊处方开具时间小于处方明细的开始时间导致系统异常 < > ="""

    @pytest.mark.parametrize('xml_name', ['audit721_1', 'audit721_2', 'audit721_3'])
    def test_recipe_small(self, mz, xml_name):
        """recipe_time<start_time,recipe_time>start_time,recipe_time=start_time均产生待审任务"""
        mz.send.send('opt', xml_name, 1)
        assert (mz.selNotAuditOptList(1))['data']['optRecipeList']