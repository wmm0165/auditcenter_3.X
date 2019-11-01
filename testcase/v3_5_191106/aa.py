# -*- coding: utf-8 -*-
# @Time : 2019/11/1 16:23
# @Author : wangmengmeng
from common.connect_db import ConnectDB
from config.read_config import ReadConfig
conf = ReadConfig()
db = ConnectDB()
def touxi_database(pid):
    conn = db.connect(db.db_sf_full)
    cur = db.get_cur(conn)
    sql = conf.get('sql', 'dialysis')
    print(sql)
    dialysis = db.execute_pid(cur, sql, pid)
    return dialysis


print(touxi_database(1572531748000))
