# -*- coding: utf-8 -*-
# @Time : 2019/10/31 9:59
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
    conn = db.connect(db.db_sf_full)
    cur = db.get_cur(conn)
    sql = conf.get('sql', 'dialysis')
    dialysis = db.execute_pid(cur, sql, pid)
    return dialysis


class TestIptTouXi:
    """AUDIT-757 是否透析"""

    @pytest.mark.parametrize("is_use,value,expected", [(1, 1, 1), (0, 1, None), (1, 0, 0), (0, 0, None)])
    def test_touxi_null(self, zy, touxi_config, is_use, value, expected):
        touxi_config.alter_default_setting(87, 'whether_dialysis', '是否透析', is_use, value)
        time.sleep(5)
        zy.send.send('ipt', 'audit757_1', 1)
        time.sleep(1)
        actual = touxi_database(zy.send.change_data['{{ts}}'])
        print(actual)
        print(expected)
        assert actual == expected

    # @pytest.mark.parametrize("is_use,value,expected", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)])
    # def test_touxi_zero(self, zy, touxi_config, is_use, value, expected):
    #     touxi_config.alter_default_setting(88, 'whether_dialysis', '是否透析', is_use, value)
    #     zy.send.send('ipt', 'audit757_2', 1)
    #     actual = touxi_database(zy.send.change_data['{{ts}}'])
    #     assert actual == expected
    #
    # @pytest.mark.parametrize("is_use,value,expected", [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)])
    # def test_touxi_one(self, zy, touxi_config, is_use, value, expected):
    #     touxi_config.alter_default_setting(88, 'whether_dialysis', '是否透析', is_use, value)
    #     zy.send.send('ipt', 'audit757_3', 1)
    #     actual = touxi_database(zy.send.change_data['{{ts}}'])
    #     assert actual == expected


if __name__ == '__main__':
    pass
