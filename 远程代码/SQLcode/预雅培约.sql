查询    AbbottDiabetesWeChat

		预约信息查询
		
		SELECT * FROM dbo.WxShopDuty

		SELECT * FROM WXShop where datatype=3
		
		
	短信接口
	
	SELECT TOP 100 * FROM AbbottDiabetesWeChat.dbo.MiniAppLog WHERE LogName='apiClient-GetSMSCode' and url like '%18817801679%'   ORDER BY id DESC
		
	SELECT TOP 100 * FROM AbbottDiabetesWeChat.dbo.MiniAppLog WHERE LogName='apiClient-GetSMSCode'  ORDER BY id DESC
	

		
自由能量行   Abbott_App

		查 id

		select * FROM Customer WHERE NickName like'%nove%'   --  oiNZm0nfm0oIRJIAItsOcx2dGKTY
		
		select * FROM Customer WHERE NickName like'%那路%'  --  oiNZm0pkAdIG-0nQIu-_5zJWMps8

		查昵称

		select * FROM Customer WHERE id='oiNZm0pkAdIG-0nQIu-_5zJWMps8' or id='oiNZm0tMVxgMWrQha-bouDch7xTg'

		delete from customer where id='oiNZm0l0hs5IReQyVhFI8lczbvT0'


		根据id查绑定的好友  双向

		select * from [dbo].[Run_UserFriend] WHERE Inviter='oiNZm0p_e31SvrTUi7bgOlANg1uM' or Inviter='oiNZm0l0hs5IReQyVhFI8lczbvT0'

		删除绑定的好友

		DELETE  FROM Run_UserFriend WHERE beInviter='oiNZm0l0hs5IReQyVhFI8lczbvT0' and inviter='oiNZm0pkAdIG-0nQIu-_5zJWMps8'

		刷能量

		select * from Run_EnergyRecord where userid='oiNZm0r6gvU4-i4_n3jtWuHp8Of0'
		
		insert into Run_EnergyRecord (userid,sourcetype,val,total) VALUES ('oiNZm0r6gvU4-i4_n3jtWuHp8Of0','5','10000000','10016839')

		刷一人团
		
		select * from [dbo].[Run_Team] where id=117 or id=118    --    oiNZm0p_e31SvrTUi7bgOlANg1uM
		
		update [Run_Team] set StartDate='2019-05-28',EndDate='2019-05-31' ,status=1 where id=121
		
		update [Run_Team] set StartDate='2019-05-07',EndDate='2019-05-10'  where id=131


		select * from Run_TeamUser where TeamId=46
		
		--update Run_TeamUser set Status= 0 where TeamId=79
		
		--TeamType:单人挑战=0,三人团=1,五人团=2
		--TeamStatus:招募中=0,已开始=1,已达成=2,未达成 = 3,已解散 =4
		--TeamUserStatus:正常=0,已退出=1,已结算=2

		目前的全部团  openID   -- oiNZm0udHtEdvRn9s7-1nM_tDAgg
		
		select t.Id,t.Type,t.Status,t.TeamUserStatus,t.StartDate,t.EndDate,t.CreatorUser,
		DATEDIFF(day,t.StartDate,getdate())StartDays,DATEDIFF(day,t.StartDate,t.EndDate)TaskDays,
		case when t.Status in (0, 4) then 0 
		else (select SUM(s.Step) 
				from Run_TeamUser u 
				left join Run_Step s on u.UserId = s.UserId 
				where s.RunDate between t.StartDate and t.EndDate and u.TeamId =t.Id and u.Status=0) end as TotalStep 
		from(
		select t.*,u.Status as TeamUserStatus,ROW_NUMBER()over(partition by t.Type order by case when t.status = 0 then '20990101' else t.StartDate end desc ) RN
		from Run_TeamUser u 
		left join Run_Team t on u.TeamId = t.Id 
		where u.UserId='oiNZm0pkAdIG-0nQIu-_5zJWMps8' and t.status<>4  -- and u.Status=0
		)t
		where t.rn = 1
		
		刷步数
		
		select *from Run_Step where userid='oiNZm0nfm0oIRJIAItsOcx2dGKTY' and rundate='2019-05-13'
		
		update Run_Step set step=315000  where  userid='oiNZm0nfm0oIRJIAItsOcx2dGKTY' and rundate='2019-05-10'
		
		删领取实物
		
		select * from Run_MyPrize where UserId='oiNZm0pkAdIG-0nQIu-_5zJWMps8' and GoodsId=1

		select * from [dbo].[Run_Goods]
		
		刷平均步数和天数等
		
		SELECT * from Run_Days where userid='oiNZm0pkAdIG-0nQIu-_5zJWMps8'
		
		update Run_Days set RunAvgStep=12345 where userid='oiNZm0pkAdIG-0nQIu-_5zJWMps8'
		
		UPDATE [dbo].[Run_Days] SET [RunDate] = '2019-05-24', [RunDay] = 4, [RunAvgStep] = 236274, [PassPercent] = 100, [CreatorTime] = '2019-05-24 10:43:33.377' WHERE [UserId] = 
		
		'oiNZm0nfm0oIRJIAItsOcx2dGKTY';
		
相册 Abbott_App
	
	formid 
	
	select * from  WeChatFormId where openid='oFNDi5IeLZUJ56bOU71Bjd-K5guA' ORDER BY ExpiresIn desc

	删除用户  Abbott_App

	select * from  CustomerConfig  where unionid='oiNZm0iYIzON2yOjrQahMKpxM71g'
	
	DELETE from CustomerConfig where unionid='oiNZm0iYIzON2yOjrQahMKpxM71g'

妇女节    AbbottDiabetesWeChat

	查看邀请的哪些人 
	
	select * from MGMMiniFans where Nickname like '%nova%' --oiNZm0qk4FzMo3YsmSO6kMUgGQEU
	
	SELECT * from  MGMInviteRegister where FriendUnionId='oiNZm0pkAdIG-0nQIu-_5zJWMps8'
	
	查看日志
	
	select top 500 * from MiniAppLog order by id desc
	
	SELECT TOP 100 * FROM AbbottDiabetesWeChat..MiniAppLog WHERE LogName='apiClient-Register' ORDER BY id DESC

春雨 AbbottDiabetesWeChat

	升级卡券
	
	
	春雨咨询过期
	
		select * from CYServiceRedeem  where unionid='oiNZm0nfm0oIRJIAItsOcx2dGKTY'
		
		DELETE from CYServiceRedeem  where unionid='oiNZm0nfm0oIRJIAItsOcx2dGKTY'


回访 

		select  top 50 * from OrderDetailImport 
		
		select top 5000 * from CSRNewCustomer order by id desc

			修改预约时间
			
		select * from ReserveRecord where reservecode='e3c84c64f95f337f'
		
		update ReserveRecord set ReserveStartTime='2019-06-04 15:30:00.000',ReserveEndTime='2019-06-04 16:00:00.000' where reservecode='e3c84c64f95f337f'
		
		
		
		