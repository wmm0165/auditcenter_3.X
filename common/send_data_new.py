# -*- coding: utf-8 -*-
# @Time : 2019/8/6 14:56
# @Author : wangmengmeng
import os
from common.request import HttpRequest
from common.tools import Tool
from config.read_config import ReadConfig
import time

def wait(func):
    # func(*args, **kw)可以使函数适配任意多的参数
    def wrapper(*args, **kw):
        time.sleep(3)
        return func(*args, **kw)

    return wrapper
class SendData:
    def __init__(self):
        self.conf = ReadConfig()
        self.tool = Tool()
        self.change_data = {"{{ts}}": str(self.tool.get_ts(0, 0)),  # 今天时间戳
                            "{{tf2}}": str(self.tool.get_ts(-1, -2)),
                            "{{tf1}}": str(self.tool.get_ts(-1, -1)),
                            "{{t}}": str(self.tool.get_ts(-1, 0)),  # 昨天时间戳
                            "{{d}}": str(self.tool.get_date(-1, 0)),  # 昨天时间
                            "{{tf3}}": str(self.tool.get_ts(-1, -3)),
                            "{{df4}}": str(self.tool.get_date(-1, -4)),
                            "{{tb1}}": str(self.tool.get_ts(-1, +1)),
                            "{{db1}}": str(self.tool.get_date(-1, +1)),
                            "{{tsb1}}": str(self.tool.get_ts(+1, 0)),  # 明天时间戳
                            "{{dtb1}}": str(self.tool.get_date(+1, 0)),  # 明天时间
                            "{{gp}}": str(self.tool.get_random(1, 10000)),
                            "{{cgp}}": str(self.tool.get_random(1, 100000)),
                            "{{ggp}}": str(self.tool.get_random(1, 1000000)),
                            "{{df6}}": str(self.tool.get_date(-1, -6)),
                            "{{df3}}": str(self.tool.get_date(-1, -3)),
                            "{{df2}}": str(self.tool.get_date(-1, -1)),
                            "{{df1}}": str(self.tool.get_date(-1, -1)),
                            "{{dt}}": str(self.tool.get_date(0, 0)),  # 今天时间
                            "{{f5}}": str(self.tool.get_date(-5, 0)), # 5天前
                            "{{f4}}": str(self.tool.get_date(-4, 0)), # 4天前
                            "{{f3}}": str(self.tool.get_date(-3, 0)), # 3天前
                            "{{f2}}": str(self.tool.get_date(-2, 0)), # 2天前
                            "{{f1}}": str(self.tool.get_date(-1, 0)),  # 5天前
                            "{{f6}}": str(self.tool.get_date(-6, 0)),  # 4天前
                            "{{f7}}": str(self.tool.get_date(-7, 0)),  # 3天前
                            "{{f8}}": str(self.tool.get_date(-8, 0)),  # 2天前
                            "{{endtoday}}":str(self.tool.get_endtoday())
                            }
    @wait
    def send(self, dir_name, xml_name, type):
        """
        审方发数据的接口
        :param dir_name:
        :param xml_name:
        :param type: 1：开具医嘱或处方 2：撤销医嘱或删除处方 3：医生双签医嘱或双签处方 4：删除处方的另外一个接口
        :return:
        """
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', dir_name, xml_name)
        url = ''
        if type == 1:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/auditcenter'
        elif type == 2:
            url = self.conf.get('auditcenter', 'address') + "/api/v1/cancelgroupdrug"
        elif type == 3:
            url = self.conf.get('auditcenter', 'address') + "/api/v1/doublesign"
        else:
            url = self.conf.get('auditcenter', 'address') + "/api/v1/cancelRecipe"

        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in self.change_data:
            ss = ss.replace(k, self.change_data[k])
        print(ss)
        return HttpRequest.post_xml(url, ss)

send = SendData()
# send.send('opt', '处方a', 1)
# send.send('opt', '修改处方a的处方头', 1)
if __name__ == '__main__':
    s = SendData()
    s.send('ipt', '多组医嘱', 1)
