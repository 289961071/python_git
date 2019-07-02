#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))
con = pymssql.connect(host=d['test_server'],port=d['test_port'], user=d['test_user'], password=str(d['test_pwd']), database=d['ks_db'])
cuesor = con.cursor()
def shanchu(shouji):
    # 先查信息
    cuesor.execute(" select  id,openid,unionid  from sysuserinfo where  Mobile=%s "%shouji)
    row = cuesor.fetchall()
    print(row)
    sql=[
    # 删除所有卡券
    "DELETE from BusCoupon where openid=%s"%row[0][1],
    # 删除短信 因为短信不回重复发
    "DELETE from SmsRecord where mobile=%s "%shouji,
    # 删除交易数据
    "DELETE  FROM TEMP_ALL_V WHERE VIP_Mobile=%s "%shouji,
    # 删除粉丝表 视情况而定，如果删除，一定要取关
    # "DELETE  from WXFans where  OpenId=%s"%row[0][1],
    # 删除会员附表
     "DELETE  FROM UserAttribute  WHERE userid=%s"%row[0][0],
    # 删除会员主表
    "delete from sysuserinfo where  Mobile=%s "%shouji,
    # 删除新客礼
    "delete from NewCustCoupon where mobile=%s "%shouji,
    # 删除生日礼
    "delete from ChgVipLevelHis where Mobile=%s "%shouji,
    # 删除模板消息 视情况
    #"delete from WXTemplateMsgSend where FansOpenId=%s "%row[0][1]
    ]
    try:
        for i in sql:
            r=cuesor.execute(i)
            print(r)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)
def xinkeli(shouji):
    # 先查信息
    cuesor.execute(" select  id,openid,unionid  from sysuserinfo where  Mobile=%s "%shouji)
    row = cuesor.fetchall()
    print(row)
    sql=[
     # 设置 LevelExpiredDate会员到期日期  级别
     "update UserAttribute set LevelExpiredDate='2019-07-27 00:00:00',Level=4 where UserId=%s"%row[0][0],
    # 删除卡券  可以选择不删除
     "delete  from BusCoupon where openid=%s"%row[0][1],
    # 删除短信
     "DELETE  from SmsRecord where  mobile =%s "%shouji,
    # 删除以前的生日礼
     "DELETE  from NewCustCoupon where  mobile =%s "%shouji,
    # 新建生日礼  mobile openid unionID
    "INSERT INTO [dbo].[NewCustCoupon]( [mobile], [openid], [unionid], [CouponPack], [CreateTime]," \
           " [CouponState], [SendTime], [GetTime], [FirstBuyTime], [FansUpdateTime], [FirstConnState], [FirstConnTime], " \
           "[SecondConnState], [SecondConnTime], [ThirdConnState], [ThirdConnTime], [MemberTime], [vip_type]) VALUES " \
           "(%s, %s, %s, 1, " \
           "'2019-04-01 18:25:01.623', 0, NULL, NULL, '2019-03-26 22:07:04.793', '2019-04-01 18:25:01.623', " \
           "2, '2019-04-01 18:33:06.063', 2, '2019-04-01 18:51:53.907', 2, '2019-04-01 18:37:40.733', '2019-04-01 18:25:01.623'," \
           " '金卡会员')"%(shouji,row[0][1],row[0][2]),
    # 更新day2day7 day60  更新发送的卡  以及 卡券类型
    "update NewCustCoupon set FirstBuyTime='2019-06-27 00:00:00',FirstConnState=0,SecondConnState=0,ThirdConnState=0,vip_type='钻卡会员'," \
         "couponpack=23,CouponState=0 where mobile=%s "%shouji,
    # 删除执行 存储
    "exec sp_genMsg4NewCust"
    ]
    try:
        for i in sql:
            cuesor.execute(i)
            print(row)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)
def jiaoyi(shouji):
    # 先查信息
    cuesor.execute("select  id,openid,unionid  from sysuserinfo where  Mobile=%s "%shouji)
    row = cuesor.fetchall()
    print(row)
    sql=[
        # 删除之前的交易记录
        # "delete BusOrderDetail where SysUserInfoId=%s"%row[0][0]
    # 设置 门店 1 kss02202    2 kss02802    物品  323  147  699  交易记录可以叠加  交易时间 必须是12个月内
    "INSERT INTO [BusOrderDetail]([BusProductId], [Quantity], [Price], [Total], [TransactionTime], [WXShopId], [SysUserInfoId], " \
    "[CreateId], [CreateTime], [UpdateId],[UpdateTime], [BatchNumber], [BusOrderDetailImportId], [UniqueNumber], [Remark],[DiscountAmount]," \
    " [StyleSize], [ShopCode], [OrderNo], [OriginalPrice], [DiscountCode], [DiscountDesc], [Point], [PointExpiredDate]) VALUES " \
    "( %d, 1, 500.0000, 500.0000,'2019-01-09 12:58:00.000', 1, %s, 0, '2019-02-03 02:00:27.963', 0, '2019-02-03 02:00:27.963',\
	    N'20180130090204878', 7666431, N'KSS02110000069581', N'',\
		 .0000, N'', %s, N'00006958', .0000, N'', N'', 500, '2020-01-09 12:58:00.000')"%(323,row[0][0],'kss02802')

    ]
    try:
        for i in sql:
            cuesor.execute(i)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)
def shengrili(shouji):

    # 先查信息 生日礼
    cuesor.execute("select  id,openid,unionid  from sysuserinfo where  Mobile=%s "%shouji)
    row = cuesor.fetchall()
    print(row)
    # 设置 生日 根据当前月份  门店 正价还是 奥莱
    sql=[
    "UPDATE sysuserinfo SET birthday='2018-07-01',activeshopcode='kss02301' where Mobile=%s "%shouji,
    # 删除卡券
    "delete  from BusCoupon where openid=%s"%row[0][1],
    # 更新等级 会员到期时间
    "UPDATE UserAttribute set Level=3 , LevelExpiredDate='2019-07-27 00:00:00' where UserId=%s"%row[0][0],
    "delete  from ChgVipLevelHis where Mobile=%s "%shouji,
    # ChgVipLevelHis VipLevel等级决定你拿什么样的生日礼
     "INSERT INTO [ChgVipLevelHis]( [SysUserInfoId], [Mobile], [VipLevel], [VipDate], [ExpiryDate], [UpgradeType], [Points], [CreateTime],"
     " [Remark]) VALUES ( %s, %s, 3, '2019-07-01', '2019-08-01', 'routine', 9999, '2019-06-25 00:00:00.000', '手工测试')"%(row[0][0],shouji),
    "exec sp_genMsg4Birthday_M1"
    ]
    try:
        for i in sql:
            cuesor.execute(i)
    except Exception as e:
        con.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        con.commit()  # 事务提交
        print('事务处理成功', cuesor.rowcount)

def cs(shouji):
    cuesor.execute("select  id,openid,unionid  from sysuserinfo where  Mobile=%s "%shouji)
    row = cuesor.fetchall()
    cuesor.execute("update UserAttribute set Level=2 where UserId=%s"%row[0][0])
    cuesor.nextset()
    row1 =con.commit()
    print(cuesor.rowcount)
shanchu('18501703352')
cuesor.close()
con.close()
