#!/usr/bin/python
# -*- coding:utf8 -*-
import requests, json
from selenium import webdriver


def fasong(shouji, msg):
    canshu = {
        "account": "N3650153",
        "password": "Y1jCG2igZa103a",
        "phone": "17788031539",
        "report": "true",
        "msg": "【katespade】尊敬的用户，您的验证码为99727，请及时输入。"
    }
    r2 = requests.post(url='https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + token,
                       data=json.dumps(canshu))
    return r2.json()


msg = {

        }
urls1 = {
    '电子券到账通知': 'eFVp1OQfypT7cD8cYGqwZgsJzHm4CiJn29D0m4_PRVg'
}
u = urls1.__len__()
print(u)

for i in urls1:
    data = fasong(openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As', url=urls1[i], token=token)
    if data['errmsg'] != 'ok':
        print('错误模板id:', i, '错误信息', data)
    else:
        print(data)
