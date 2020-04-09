# -*- coding: utf-8 -*-
# @Time : 2020/4/2 10:01
# @Author : wangmengmeng
import pytest
from common.alter_config import AlterConfig
from common.opt import Opt

@pytest.fixture(scope="session",autouse=True)
def opt_huanzhe():
    """修改配置项-门诊处方审查模式 为按患者"""
    ac = AlterConfig()
    ac.alter_sys_config(40041, 2)


@pytest.fixture(scope='function')
def mz():
    opt = Opt()
    yield opt
    print("门诊用例执行结束...")
