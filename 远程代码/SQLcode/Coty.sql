   数据库  Wedo.Wx
	 
	 user wedo  --  state=0 未使用权益  1已使用权益  result 抽奖结果0未中奖 1正装 2 积分
	 
	 insert into CotyRightsInfo values(17788031539,'o7_NJuCSJmLSkAhlaW_q-fwN3uh4',3,17201266,172,4,1,0,0,NULL)
	 
	 select top 10 * from CotyRightsInfo  where mobile='17788031539' ORDER BY id desc  --  98925460
	 
	 INSERT INTO [CotyRightsInfo]( [Mobile], [Openid], [BrandId], [UserId], [CrmEventDataId], [CampaignId], [RightType], [State], [Result], [UsedTime]) VALUES ( N'18501709317', N'o7_NJuJiBJKThlxCJQc7zuxgyvcw', 3, 0, 172, 4, 1, 0, 0,null);

 抽奖次数
 
 update CotyRightsInfo set state=0,Result=0 where mobile in ('17788031539')
 
	 粉丝表
	 
	  select top 10 * from WxFans where openid='o7_NJuHuABLtZ8a_bAc7cKQFouiY'   --  nickname like '%那路逗%'  98925458
		
		 select top 10 * from WxFans where  nickname like   '%p20pro%' or nickname like '%iPhoneX18501707917%'
		 
		 select id,openid,userid from WxFans where  nickname like '%那路逗%'
		 
		 未注册设置
		 
		 update WxFans set userid=0 where Nickname like '%那路逗%'
		 
		 会员等级
		 
		 核销
		 
		 select * from CotyCounter where counter_name like '郑州%'
		 
		 select * from WxQrcode where StoreCode ='MF0HN2020'
		 
		 select * from WxQrcode where url='http://weixin.qq.com/q/027BsRYSLP99U10000007Q'
		 
		 预约  particiipationtype  2是明星装 1 是预约装
		 
		 select top 10 * from CotyCampaignParticipation ORDER BY id desc --  98925460
		 
		 delete from CotyCampaignParticipation where userid='98925460'
		 