# -*- coding: utf-8 -*-
# @Time : 2019/8/6 16:28
# @Author : wangmengmeng
from common.request import HttpRequest
from config.read_config import ReadConfig
from common.send_data import SendData
import time


def wait(func):
    # func(*args, **kw)可以使函数适配任意多的参数
    def wrapper(*args, **kw):
        time.sleep(3)
        return func(*args, **kw)

    return wrapper


class Ipt:
    def __init__(self):
        self.send = SendData()
        self.conf = ReadConfig()
        self.request = HttpRequest()

    @wait
    def selNotAuditIptList(self):
        """
        待审住院列表根据患者号查询
        :return:   通过return结果可以获得以下数据：engineid res['data']['engineInfos'][0]['id']
        """
        # self.send.send('ipt', '医嘱一', 1)
        # time.sleep(3)
        url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/selNotAuditIptList'
        param = {
            "patientId": self.send.change_data['{{ts}}']
        }
        res = self.request.post_json(url, param)
        return res

    def get_engineid(self, n):
        """
        待审列表获取引擎id
        :param n: 如果某患者有多条待审任务则会有多个引擎id，n代表取第几个引擎id
        :return:
        """
        res = self.selNotAuditIptList()
        return res['data']['engineInfos'][n - 1]['id']

    def audit_multi(self, *ids):
        """
        待审住院任务列表批量通过
        :param ids:  引擎id
        """
        url = self.conf.get('auditcenter', 'address') + '/api/v1/auditBatchAgree'
        param = {
            "ids": ids,
            "auditType": 3,  # 3指住院
            "auditWay": 2
        }
        self.request.post_json(url, param)

    def ipt_audit(self, gp, engineid, audit_type):
        """
        医嘱详情审核任务
        :param gp:
        :param engineid:
        :param audit_type: 0 审核打回  1 审核打回（可双签） 2 审核通过
        orderType : 1：药物医嘱； 2：非药物医嘱；3：草药医嘱
        """
        url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/auditSingle'
        param = ''
        if audit_type == 0:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "必须修改",
                    "auditStatus": 0,
                    "engineId": engineid,
                    "orderType": 1
                }]
            }
        elif audit_type == 1:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "打回可双签",
                    "auditStatus": 0,
                    "engineId": engineid,
                    "orderType": 1,
                    "messageStatus": 1
                }]
            }
        elif audit_type == 2:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "审核通过",
                    "auditStatus": 1,
                    "engineId": engineid,
                    "orderType": 1
                }]
            }
        self.request.post_json(url, param)

    def orderList(self, engineid, type):
        """
        获取药嘱信息
        :param engineid:
        :param type: 0 待审页面 1 已审页面
        :return:
        """
        if type == 0:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/orderList' + '?id=' + str(engineid)
        else:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/all/orderList' + '?id=' + str(engineid)
        return self.request.get(url)

    def herbOrderList(self, engineid, type):
        if type == 0:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/herbOrderList' + '?id=' + str(engineid)
        else:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/all/herbOrderList' + '?id=' + str(engineid)
        return self.request.get(url)

    def get_patient(self, engineid, type):
        """获取住院患者信息"""
        if type == 0:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/iptPatient' + '?id=' + str(engineid)
        else:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/all/iptPatient' + '?id=' + str(engineid)
        return self.request.get(url)

    def get_operation(self, engineid, type):
        """获取住院手术信息"""
        if type == 0:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/operationList' + '?id=' + str(engineid)
        else:
            url = self.conf.get('auditcenter', 'address') + '/api/v1/ipt/all/operationList' + '?id=' + str(engineid)
        return self.request.get(url)



if __name__ == '__main__':
    ipt = Ipt()
    ipt.send.send('ipt', '医嘱一', 1)
    ipt.send.send('ipt', '医嘱二', 1)
    res = ipt.get_engineid(1)
    print(res)
    res =ipt.get_engineid(2)
    print(res)
