查询    AbbottDiabetesWeChat

		预约信息查询
		
		SELECT * FROM dbo.WxShopDuty

		SELECT * FROM WXShop where datatype=3
		
		select * from CRMUser where mobile='13817187785'
		
	短信接口
	
	SELECT TOP 100 * FROM AbbottDiabetesWeChat.dbo.MiniAppLog WHERE LogName='apiClient-GetSMSCode' and url like '%18817801679%'   ORDER BY id DESC
		
	SELECT TOP 100 * FROM AbbottDiabetesWeChat.dbo.MiniAppLog WHERE LogName='apiClient-GetSMSCode'  ORDER BY id DESC
	

		
自由能量行   Abbott_App

		查 id

		select * FROM Customer WHERE NickName like'Polaris%'   --  oFNDi5A4W-YF7rLivSeRVDVLjeL0   ogb9a1I6Uj7_K4HjFg53cry3U2cE
		
		select * FROM Customer WHERE NickName like'那路逗%'  --  oiNZm0vVGix4AM8OCnC7srAR2iYA

		查昵称

		select * FROM Customer WHERE id='ogb9a1FselRKRTlCdCe0N3qoRMXM' 
		
		delete from customer where id='oiNZm0l0hs5IReQyVhFI8lczbvT0'


		根据id查绑定的好友  双向

		select * from [dbo].[Run_UserFriend] a  ,Customer c join   WHERE Inviter='ogb9a1GH3P0MiWSyMWoF_BAec_3o' 
		
		select * from Run_UserFriend  WHERE Inviter='ogb9a1GH3P0MiWSyMWoF_BAec_3o' or BeInviter='ogb9a1GH3P0MiWSyMWoF_BAec_3o'
		
		order by inviter
		
		删除绑定的好友

		DELETE  FROM Run_UserFriend WHERE beInviter='oiNZm0l0hs5IReQyVhFI8lczbvT0' and inviter='oiNZm0pkAdIG-0nQIu-_5zJWMps8'

		刷能量  SourceType
    {
        兑换奖品 = 1,
        参与挑战 = 2,
        点赞 = 3,
        邀请好友 = 4,
        步数增加 = 5
    }

		select * from Run_EnergyRecord where userid='ogb9a1GH3P0MiWSyMWoF_BAec_3o' and SourceType=4
		
		select * from Run_EnergyRecord where total > '1000000'
		
		select * from Run_MyPrize where goodsid=1
		
		insert into Run_EnergyRecord (userid,sourcetype,val,total) VALUES ('oiNZm0pkAdIG-0nQIu-_5zJWMps8','5','10000000','10012554')

		刷一人团
		
		select * from [dbo].[Run_Team] where id=138   --    oiNZm0p_e31SvrTUi7bgOlANg1uM
		
		update [Run_Team] set StartDate='2019-05-28',EndDate='2019-05-31' ,status=1 where id=121
		
		update [Run_Team] set StartDate='2019-05-07',EndDate='2019-05-10'  where id=138


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
		where u.UserId='ogb9a1N1ecXelruHJiy4Ls9Kr-FA' and t.status<>4  -- and u.Status=0
		)t
		where t.rn = 1
		
		
		
		刷步数
		
		select *from Run_Step where userid='ogb9a1OGFWkV1MdNddzLlAgq8iNQ' and rundate='2019-06-12'
		
		update Run_Step set step=315000  where  userid='oiNZm0udHtEdvRn9s7-1nM_tDAgg' and rundate='2019-06-12'
		
		INSERT INTO Run_Step VALUES ('oiNZm0udHtEdvRn9s7-1nM_tDAgg', '2019-06-11', 315000, '2019-06-11 13:55:17.923', '2019-06-11 13:55:17.923', '0', NULL, 0);

		删领取实物
		
		select * from Run_MyPrize where GoodsId=1  UserId='oiNZm0pkAdIG-0nQIu-_5zJWMps8' and GoodsId=1

		select * from [dbo].[Run_Goods]
		
		刷平均步数和天数等
		
		SELECT * from Run_Days where userid='ogb9a1OGFWkV1MdNddzLlAgq8iNQ'
		
		update Run_Days set RunAvgStep=12345 where userid='oiNZm0pkAdIG-0nQIu-_5zJWMps8'
		
		UPDATE [dbo].[Run_Days] SET [RunDate] = '2019-05-24', [RunDay] = 4, [RunAvgStep] = 236274, [PassPercent] = 100, [CreatorTime] = '2019-05-24 10:43:33.377' WHERE [UserId] = 
		
		'oiNZm0nfm0oIRJIAItsOcx2dGKTY';
		
相册 Abbott_App
	
	formid  
	
	select *  from  WeChatFormId where openid='o-3vr4uLUsCQ_rK-f9Mw3WZ-NGqM' ORDER BY ExpiresIn desc
	
	

	删除用户  Abbott_App

	select * from  CustomerConfig  where unionid='oiNZm0pkAdIG-0nQIu-_5zJWMps8'  --  oiNZm0ik1E56gx7HBEwMVF2MTWp0    那路逗
	
	select * from  CustomerConfig  where unionid='oiNZm0ik1E56gx7HBEwMVF2MTWp0' 
	
	DELETE from CustomerConfig where unionid='oiNZm0pkAdIG-0nQIu-_5zJWMps8'
	
	触发模板消息
	
	INSERT INTO [AbbottDiabetesWeChat].[dbo].[WXTemplateMsgSend]
    ([MsgInfoId]
    ,[SysUserInfoId]
    ,[PlatformOpenId]
    ,[FansOpenId]
    ,[DataJson]
    ,[Url]
    ,[ProcessStatus]
    ,[ProcessPlanTime]
    ,[IsTimely]
    ,[MiniProgramAppid]
    ,[MiniProgramPagePath]
    ,[TemplateId]
    )

           SELECT w.Id [MsgInfoId]
                 ,0 [SysUserInfoId]
                 ,w.[PlatformOpenId]
                 ,t.OpenId [FansOpenId]
                 ,replace(replace(Content,
                 '{Nickname}',t.NickName),
                 '{JoinDate}', CONVERT(nvarchar(10),GETDATE(),120)) DataJson
                 ,[Url]
                 ,1 [ProcessStatus]
                 ,GETDATE() [ProcessPlanTime]
                 ,1 [IsTimely]
                 ,[MiniProgramAppid]
                 ,[MiniProgramPagePath]
                 ,'' [TemplateId]
             FROM [AbbottDiabetesWeChat].dbo.WXMessageInfo w WITH (NOLOCK)
                 ,(
                  SELECT distinct c.NickName
                        ,w.OpenId
                    FROM [dbo].[Customer] c WITH (NOLOCK)
                         INNER JOIN dbo.Run_User r WITH (nolock) ON c.Id = r.UserId
                         INNER JOIN AbbottDiabetesWeChat.dbo.WXFans w with(NOLOCK) on r.UserId = w.UnionId
                         LEFT JOIN dbo.Run_Step s WITH (nolock) ON r.UserId = s.UserId
                                                                   --AND s.RunDate = CAST(GETDATE() AS date)
                    WHERE c.NickName in('Polaris','赛门LHJ')
                  ) t
             WHERE w.MsgType = 'templet'
                   AND w.Description = 'templet_warn'
									 
									 

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
		
		
		新客老客
		
		select * from CSRNewCustomer where mobile='13428992880' ORDER BY id desc   -- 新客
		
		select *from SysUserInfo where Mobile='13817187785'
		
		select top 10 * from [dbo].[CRMTaggedUser] where CustomerMobile='13509690202' ORDER BY id desc --老客
		
		INSERT INTO []([Id], [Mobile], [Source], [Channel], [HCPCode], [OrderHCPCode], [IsBuy], [IsBuyReader], [IsTYHBuy], [CreateTime], [OrderNo], [OrderTime], [LastUpdateTime], [ControlGroup], [ValidateWay], [ConvertTime], [UniqueNumber], [IsTYHNewCustomer]) VALUES (5016, '98957526699', N'3', N'微商城', 'HCP-Shanghai-Rep-1', 'HCP-Shanghai-Rep-1', NULL, NULL, NULL, '2018-11-13 18:06:40.450', N'20181534055304380D6jxiS', '2018-07-13 17:53:41.000', '2018-11-13 18:06:40.450', 0, 'CSR', NULL, N'20181534055304380D6jxiS_WS00S01C00_3', '1');

		INSERT INTO [CRMTaggedUser]( [BatchNo], [TagName], [CustomerId], [CustomerMobile], [CustomerName], [OrderSource], [OrderDate], [ProcessStatus], [ProcessResult], [CreateTime], [UpdateTime]) VALUES ( N'20190228', N'lapsed', N'dc6ce663-c1dd-e81133', N'98343067980', N'杨光', N'天猫', '2018-11-03', 2, N'OK', '2019-02-28 16:28:59.323', '2019-02-28 16:28:59.970');

	密码修改  --   tPnkk6WSeOYM+
	
	select Password,*
	--update su set su.Password = upper(SUBSTRING(master.dbo.fn_varbintohexstr(HashBytes('MD5','tPnkk6WSeOYM+')), 3, 32) ),su.LoginFailures = 0
from SysUserInfo su with(nolock)
where su.LoginFailures > = 10 and name='admin'

购买记录 -- 15162986259  13922100177

log日志

select top 10 * from logapi


