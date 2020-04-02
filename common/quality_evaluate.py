# -*- coding: utf-8 -*-
# @Time : 2019/12/25 13:56
# @Author : wangmengmeng
from common.request import HttpRequest
from config.read_config import ReadConfig


class QualityEvaluate:
    def __init__(self):
        conf = ReadConfig()
        self.auditcenter_url = conf.get('auditcenter', 'address')
        self.request = HttpRequest()

    def ipt_checklist(self, starttime, endtime, ids):
        url = self.auditcenter_url + '/api/v1/analysis/ipt/extractIptCheckData'
        param = {
            "currentPage": 1,
            "pageSize": 20,
            "startTime": starttime,
            "endTime": endtime,
            "source": "3",
            "type": "1",
            "auditIdList": ids
        }
        res = self.request.post_json(url, param)
        return res['data']

    def opt_checklist(self, starttime, endtime, ids, source):
        """
        获取抽取项目总条数
        :param starttime: 开始日期
        :param endtime: 结束日期
        :param ids: audit_doctor_id
        :param source: 门急诊：0 门诊：1 急诊：2
        :return:
        """
        url = self.auditcenter_url + '/api/v1/analysis/opt/getCheckList'
        param = {
            "currentPage": 1,
            "pageSize": 20,
            "startTime": starttime,
            "endTime": endtime,
            "source": source,
            "type": "1",
            "auditIdList": ids
        }
        res = self.request.post_json(url, param)
        return res['data']

    def opt_ResultList(self,starttime, endtime, id, source):
        """只能查到审方药师为自己的数据"""
        url = self.auditcenter_url + '/api/v1/analysis/opt/reviewResultList'
        param = {
            "pageSize": 20,
            "currentPage": 1,
            "startTime": starttime,
            "endTime": endtime,
            "source": source,
            "checkPeopleId": id
        }
        res = self.request.get_with_params(url,**param)

    def opt_ResultList1(self):
        url = self.auditcenter_url + '/api/v1/analysis/opt/reviewResultList'
        param = {
            "pageSize": 20,
            "currentPage": 1,
            "startTime": 1577203200000,
            "endTime": 1577289599000,
            "source": "0",
            "checkPeopleId": 6
        }
        res = self.request.get_with_params(url,param)
        print(type(res))
        print(res.url)
        print(res.json())
        return res

if __name__ == '__main__':
    qe = QualityEvaluate()
    print(qe.opt_ResultList1())