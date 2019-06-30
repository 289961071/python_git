#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路

import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))
con = pymssql.connect(host=d['test_server'],port=d['test_port'], user=d['test_user'], password=str(d['test_pwd']), database=d['ks_db'])
cuesor = con.cursor()
def shanchu(shouji):
    # 先查信息
    cuesor.execute(" select  id,openid,unionid  from sysuserinfo where  Mobile=%s ", shouji)
    row = cuesor.fetchall()
    print(row)
    # 删除卡券
    sql2 = "DELETE from BusCoupon where openid='"+row[0][1]+"'"
    # 删除短信
    sql1 = "DELETE from SmsRecord where mobile='"+shouji+"'"
    # 删除交易数据
    sql3 = "DELETE  FROM TEMP_ALL_V WHERE VIP_Mobile='"+shouji+"'"
    # 删除粉丝表
    sql4 = "DELETE  from WXFans where  OpenId='"+row[0][1]+"'"
    # 删除会员附表
    sql5="DELETE  FROM UserAttribute  WHERE userid='"+str(row[0][0])+"'"
    # 删除会员主表
    sql6="delete from sysuserinfo where  Mobile='"+shouji+"'"

    try:
        for i in (sql1,sql2,sql3,sql4,sql5,sql6):
            cuesor.execute(i)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)
def xinkeli(shouji):
    #先 看有没有NewCustCoupon
    # 先查信息
    cuesor.execute(" select  id,openid,unionid  from sysuserinfo where  Mobile=%s ", shouji)
    row = cuesor.fetchall()
    print(row[0][1])
    # 设置 LevelExpiredDate
    sql2 = "update UserAttribute set LevelExpiredDate='2019-07-27 00:00:00' where UserId='"+str(row[0][0])+"'"
    # 删除卡券  一看选择不删除
    sql1 = "delete  from BusCoupon where openid='"+row[0][1]+"'"
    # 更新等级
    sql3 = "update UserAttribute set Level=4 where UserId='"+str(row[0][0])+"'"
    # 删除短信
    sql4 = "DELETE  from SmsRecord where  mobile ='"+shouji+"'"
    # 更新day2day7 day60  更新发送的卡  没有要先insert
    sql5="update NewCustCoupon set FirstBuyTime='2019-06-27 00:00:00',FirstConnState=0,SecondConnState=0,ThirdConnState=0,vip_type='钻卡会员'," \
         "couponpack=23,CouponState=0 where mobile="+shouji+"'"
    # 删除执行 存储
    sql6="exec sp_genMsg4NewCust"

    try:
        for i in (sql1,sql2,sql3,sql4,sql5,sql6):
            row=cuesor.execute(sql1)
            print(row)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)
def shengrili(shouji):
    #先 看有没有NewCustCoupon
    # 先查信息
    cuesor.execute(" select  id,openid,unionid  from sysuserinfo where  Mobile=%s ", shouji)
    row = cuesor.fetchall()
    print(row[0][1])
    # 设置 生日
    sql2 = "UPDATE sysuserinfo SET birthday='2018-06-27' where Mobile='"+shouji+"'"
    # 删除卡券
    sql1 = "delete  from BusCoupon where openid='"+row[0][1]+"'"
    # 更新等级
    sql3 = "UPDATE UserAttribute set Level=4 where UserId='"+str(row[0][0])+"'"
    # ChgVipLevelHis VipLevel等级决定你拿什么样的生日礼
    sql4 = "update ChgVipLevelHis set VipLevel=4,VipDate='2019-06-01' where Mobile='"+shouji+"'"
    sql44 = "update sysuserinfo set activeshopcode='kss02301' where mobile='"+shouji+"'"
    # 更新day2day7 day60  更新发送的卡
    sql5="update NewCustCoupon set FirstBuyTime='2019-06-27 00:00:00',FirstConnState=0,SecondConnState=0,ThirdConnState=0,vip_type='粉蜜会员'," \
         "couponpack=23,CouponState=0 where mobile="+shouji+"'"
    # 删除执行 存储
    sql6="exec sp_genMsg4Birthday_M1"

    try:
        for i in (sql1,sql2,sql3,sql4,sql44,sql5,sql6):
            row=cuesor.execute(sql1)
            print(row)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)

xinkeli('15921825165')
cuesor.close()
con.close()
