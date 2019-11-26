from common.request import HttpRequest


def get_selNotAuditIptList():
    req = HttpRequest()
    url = "http://10.1.1.178:9999/auditcenter/api/v1/ipt/selNotAuditIptList"
    param = {}
    res = req.post_json(url, param)
    print(res['data']['taskNumList'])
    s = 0
    for i in res['data']['taskNumList']:
        # print(i['taskNum'])
        s += i['taskNum']
    print(s)


if __name__ == '__main__':
    get_selNotAuditIptList()
