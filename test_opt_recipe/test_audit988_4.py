# -*- coding: utf-8 -*-
# @Time : 2020/4/9 11:28
# @Author : wangmengmeng
import pytest


class TestAudit988:

    @pytest.mark.parametrize("xmlname", ['audit988_5', 'audit988_6'],
                             ids=["患者信息身高、体重为特殊字符", "患者信息身高、体重为中文"])
    def test_01(self, mz, xmlname):
        mz.send.send('opt', xmlname, 1)
        assert mz.selNotAuditOptList(1)['data']['taskNumList']  # 能正常产生待审任务
