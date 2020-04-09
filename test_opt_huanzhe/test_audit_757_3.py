# -*- coding: utf-8 -*-
# @Time : 2020/4/9 14:29
# @Author : wangmengmeng
import pytest
from common.alter_config import AlterConfig
from common.connect_db import ConnectDB
from config.read_config import ReadConfig
import time

db = ConnectDB()
conf = ReadConfig()


@pytest.fixture(scope='function')
def touxi_config():
    sc = AlterConfig()
    yield sc


def touxi_database(pid):
    """根据患者号获取数据库中透析值"""
    conn = db.connect(db.db_sf_full)
    cur = db.get_cur(conn)
    sql = conf.get('sql', 'dialysis')
    dialysis = db.execute_pid(cur, sql, pid)
    return dialysis


class TestOptTouXi:
    """AUDIT-757 是否透析"""

    @pytest.mark.parametrize("is_use,value,expected", [(0, 0, ''), (0, 1, ''), (1, 0, ''), (1, 1, '')])
    def test_touxi_null(self, mz, touxi_config, is_use, value, expected):
        """审方透析值传空"""
        touxi_config.alter_default_setting(87, 'whether_dialysis', '是否透析', is_use, value)
        mz.send.send('opt', 'audit_757_1', 1)
        time.sleep(1)
        engineid = mz.get_engineid(1)
        actual = (mz.get_recipeInfo(engineid, 0))['data']['outpatient']['dialysis']
        # actual = touxi_database(zy.send.change_data['{{ts}}'])
        print(actual)
        print(expected)
        assert actual == expected

    @pytest.mark.parametrize("is_use,value,expected", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)])
    def test_touxi_zero(self, mz, touxi_config, is_use, value, expected):
        """审方透析值传0"""
        touxi_config.alter_default_setting(87, 'whether_dialysis', '是否透析', is_use, value)
        mz.send.send('opt', 'audit_757_2', 1)
        time.sleep(1)
        engineid = mz.get_engineid(1)
        actual = (mz.get_recipeInfo(engineid, 0))['data']['outpatient']['dialysis']
        assert actual == str(expected)

    @pytest.mark.parametrize("is_use,value,expected", [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)])
    def test_touxi_one(self, mz, touxi_config, is_use, value, expected):
        """审方透析值传1"""
        touxi_config.alter_default_setting(87, 'whether_dialysis', '是否透析', is_use, value)
        mz.send.send('opt', 'audit_757_3', 1)
        time.sleep(1)
        engineid = mz.get_engineid(1)
        actual = (mz.get_recipeInfo(engineid, 0))['data']['outpatient']['dialysis']
        assert actual == str(expected)
