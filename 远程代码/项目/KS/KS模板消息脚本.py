#!/usr/bin/python
# -*- coding:utf8 -*-
import requests,json
from selenium import webdriver
def gettoken():

    re=webdriver.Chrome()
    re.get('')
def fasong(openid,url,token):
    #测试APPID：wx65d16d0e8772bac6   正式的 wx5d831b3fbcb54f75
    #测试的token  http://twechat.katespade.wedochina.cn/test/TestToken
    canshu={
        "touser": openid,
        "template_id":url,
        "url": "",
        "miniprogram": {
            "appid": "wx65d16d0e8772bac6",
            "pagepath": "pages/linkMemberCenter/linkMemberCenter"
        },
        "data": {
            "first": {
                "value": "尊敬的顾客，您已成功绑定kate spade new york官方微信。  ",
                "color": "#000000"
            },
            "keyword1": {
                "value": "(测试参数1)",
                "color": "#000000"
            },
            "keyword2": {
                "value": "(测试参数2)",
                "color": "#000000"
            },
            "keyword3": {
                "value": "(测试参数3)",
                "color": "#000000"
            },
            "keyword4": {
                "value": "(测试参数4)",
                "color": "#000000"
            },
            "keyword5": {
                "value": "(测试参数5)",
                "color": "#000000"
            },
            "name": {
                "value": "(测试参数6)",
                "color": "#000000"
            },
            "expDate": {
                "value": "(测试参数7)",
                "color": "#000000"
            },
            "number": {
                "value": "(测试参数8)",
                "color": "#000000"
            },
            "certificateNumber": {
                "value": "(测试参数9)",
                "color": "#000000"
            },
            "keynote1": {
                "value": "(测试参数9)",
                "color": "#000000"
            },
            "keynote2": {
                "value": "(测试参数9)",
                "color": "#000000"
            },

            "remark": {
                "value": "时间：2019年05月24日\n点击“详情”即可进入会员中心，查看更多会员权益！",
                "color": "#000000"
            }
        }
    }
    r2=requests.post(url='https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+token,data=json.dumps(canshu))
    return r2.json()
token='21_YHwdMDESg8X_mbiaEyzaNGHdZksphkLl4ZKFkLnyCGd_kEsT0MTiBA5T6i-E6f-Q8c4a8OGlu-H0dwFUas80rUMEZTcj13f5SaKJid1ErVTpJJmPZy2zVUB6Se1Mujnhp8l0nOvTQLjPaljTWOYjAHDDVF'
urls={'账号绑定成功提醒（非会员关注并绑定微信）':'QuWiXFuTpFZy2L3mb0dTRA-Z28pq_LlbTxcGOHteVOo',
        '绑定会员通知（线下会员关注并绑定微信）':'WI9fxlshLXNqGuFvn8YNB_M417_CYRxrIZSRqIRbqDI',
        '中奖结果通知	':'EcD9Gid3BEKHWdsAc-7ReTIVm3VU4JJ7eJ--h-EUTVo',
        '电子券到账通知':'0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI',
        '电子券到期提醒':'O0tdv3u--vmcymWDMvZMxMxkHAmCJAtjb5eoEEURnCo',
        '现金券使用通知':'s-1J54p9BIaUYoAde5-RV0NxfRbcntDlKjZDmkcYLxw',
        '会员积分提醒	':'eQFgCJjBm-ng1IFZhPdNMRrC5jcgVV_G5U-eSi8Dnb4',
        '会员到期提醒':'5Qlb9HLZyfw6a81rFHJP3_YpTTPrU9sUCqaVox0SMAI',
        '生日礼物领取提醒':'PuvNnKFUJoio1scSrzuMftqcAkmUu59StJh1ATS_Jao',
        '调研礼品领取提醒':'J_NHCUPaMnqO6XLYlYAH2RQtDgISVh7Y4TNnn_NIzPU',
        '购买成功通知	':'tZuOJXpKErv4TiC4L23-_xLMMiRGmKOGEyB1gE6I3s0',
        '预约成功通知	':'9XUGzn3PM5desbiRW10rmgpg-6DoDgUujijV3HOQ-2M',
        '服务变更通知	':'fLr-Q7TouBEGQKecqyzMlZs74OSKSJz27CiaFsIAGUg',
        '报名成功通知	':'_BaluXwSk499z8uSoHDjKYNDNJyoJ6D31gSwEZo6nT0',
        '会员卡升级通知':'hi3In3kE3Y_iBMfcCe7Tv_M99llDHWEfuiLDrty9mmY',
        '预约提醒':'yftKZRf6BYgTVjSgFVY8u3QjU6uRojJfSpK-3e5sMFU',
        '服务到期提醒	':'junI1SQFkbg7GEj6NyG8eh0IqFuaZBZlAY2HVysQAJM',
        '服务完成提醒	':'5wGAWfxTgjwJOmH3tO1hQ-tGWiRI0ZA6A2L8Bzxh0pY',
        '消费提醒':'7g9RCRex4oSWukk8XBT-EixeegsGuENCFf5_X74D2eA',
        'MGM老客活动参与成功通知':'0Lu4d1LKNnIqbs4iEaOUsotRjfDKRhpzq1Qv7QxS-8I',
        'MGM新客礼券到账通知 ':'	0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI',
        'MGM新客活动参与成功通知':'0Lu4d1LKNnIqbs4iEaOUsotRjfDKRhpzq1Qv7QxS-8I',
        'MGM老客礼券到账通知':'0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI',
        'MGM电子券到期提醒':'O0tdv3u--vmcymWDMvZMxMxkHAmCJAtjb5eoEEURnCo',
        '成为会员通知':'NFo5jajocBBc_KtjFQTgW0B9fvXia1HYEAhY-kl14Jw',
        '电子券到账提醒':'0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI',
        '新客复购电子券到期提醒':'	O0tdv3u--vmcymWDMvZMxMxkHAmCJAtjb5eoEEURnCo',
        '报名成功通知20190403':'3UjX95BxpsS072k6LzVDH7WWrGyxsmxmX7pIRX-g4MU',
        '报名成功通知20190514	':'wVz_iOU53YxNFSuvQCor-5ZFVO-7n2Vy70lKfUp5Fio'

          }
urls1={
    '电子券到账通知':'eFVp1OQfypT7cD8cYGqwZgsJzHm4CiJn29D0m4_PRVg'
}
u=urls1.__len__()
print(u)

for i in urls1:
    data=fasong(openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As',url=urls1[i],token=token)
    if data['errmsg']!='ok':
        print('错误模板id:',i,'错误信息',data)
    else:
        print(data)