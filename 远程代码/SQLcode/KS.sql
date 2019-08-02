use  katespadewechat

		粉丝表查看关注  openid
		
		select openid,sourceid,LastScanSourceId ,nickname,createtime,updatetime,* from WXFans where openid='oIH_St__uL5rk0bEgCSXCd_KbRn4'
		
		置空
		UPDATE WXFans set memberid=0 where  Nickname like '%heidi%'

		会员主表  Mobile

		select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile='18501709317'  
			UPDATE UserAttribute SET point=8000,level=3   where userid=10523703
			update sysuserinfo set usercode='KS201926275' where  Mobile='17788031539'  
		修改生日
			UPDATE sysuserinfo SET birthday='1974-06-13' where  Mobile='13816102444' 
		修改活跃门店  --正价  kss02301   奥莱  kss02202
		update sysuserinfo set activeshopcode='kss02301' where Mobile='17788031539'  
		置空openid 老客户有数据未注册
		UPDATE sysuserinfo set openid =''   where Mobile='15921825165'
		
		cs200 hmt用户 vip_tel_2
		
		select top 10 * from Raw_VIP_Full where vip_tel_2='13718879728'
		
	
		--activityshopcode 是正价 奥莱店 WXSHOP表
			
			查看正价还是奥莱
			
			select *from wxshop where code='kss02701'
			
			select * from BusProduct 
			
			select * from WXQRCodeLimit where WXSourceid=414
			select * from HMTShopBindCard where 
			
			select p.code,t.WXsourceid ,t.name,t.remark from wxshop p, WXQRCodeLimit t where p.code in ('kss02701','KSS02114') and p.id=t.wxshopid
			
		会员附表  userID就是sysuserinfo 的id

		select * from UserAttribute where userid=10510506
		
					修改领取动作
			
					UPDATE UserAttribute set iscoupon=0 where userid=510253914
					
					会员等级
					
					UPDATE UserAttribute set level=2 where userid=510253939	
					
					会员积分
		
					UPDATE UserAttribute SET point=6000,level=2   where userid=10510506
			
					生日
				
					UPDATE sysuserinfo SET birthday='2018-06-01' where Mobile='10086402'
					
					入会时间和积分 等级
		
					UPDATE UserAttribute SET MemberStartTime='2019-03-08',point=6000 ,level=2 where userid=510253851
			
		卡券 openid
				
		select top  200* from BusCoupon where sendtime>'2019-07-31' and  order by  id  desc 
			
					删除领取的卡券
				
				delete from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As'
					
					新客卡券
				select top 10 * From NewCustCoupon WHERE openid='oIH_St1cZPLTP77d4ZPgzZK1Mpj0'
		
					对应领取的卡  couponpack  状态 0是未发送 1 已发送 2 已领取
					
				update 	NewCustCoupon set couponpack=23,CouponState=0 where mobile='15921825165'
			
				修改day1 day7 day14  没有就造数据  -- oUaMnwyz7oeam8mUpdLoJoig_7Xg    o5Icn51q5Dlu-aQHu0hB2UqDniFw
			
				select * From NewCustCoupon where mobile='18017695729'
		
				select * from ChgVipLevelHis  where mobile='' --15921825165 查看有没有手机 没有就不发短信

				INSERT INTO [dbo].[NewCustCoupon]( [mobile], [openid], [unionid], [CouponPack], [CreateTime], [CouponState], [SendTime], [GetTime], [FirstBuyTime], [FansUpdateTime], [FirstConnState], [FirstConnTime], [SecondConnState], [SecondConnTime], [ThirdConnState], [ThirdConnTime], [MemberTime], [vip_type]) VALUES ('18017695729', 'oIH_St_dMLhOLB8GNr4hrCz0asYo', 'oVTmZ1GSFpXFm2_c4VLikgXSgeZA', 1, '2019-04-01 18:25:01.623', 0, NULL, NULL, '2019-03-26 22:07:04.793', '2019-04-01 18:25:01.623', 2, '2019-04-01 18:33:06.063', 2, '2019-04-01 18:51:53.907', 2, '2019-04-01 18:37:40.733', '2019-04-01 18:25:01.623', '金卡会员');
				修改dayX 必须是会员等级
				update NewCustCoupon set FirstBuyTime='2019-06-30 00:00:00',
				FirstConnState=0,SecondConnState=0,ThirdConnState=0,vip_type='金卡会员',couponpack=23,CouponState=0 where mobile='18017695729'

				发新客 短信			
				exec sp_genMsg4NewCust
				 
		生日礼  VIPDate 必须小于等于 当月.1 修改自己的生日为6月份  没有就insert
				
		select * from 	ChgVipLevelHis where mobile='18017695729'    -- ChgVipLevelHis VipLevel等级决定你拿什么样的生日礼
			
					INSERT INTO [ChgVipLevelHis]( [SysUserInfoId], [Mobile], [VipLevel], [VipDate], [ExpiryDate], [UpgradeType], [Points], [CreateTime], [Remark]) VALUES ( 10443336, 		N'18017695729', 3, '2019-07-01', '2019-08-01', N'routine', 9999, '2019-06-25 00:00:00.000', N'手工测试');
					
			发送钱先修改生日
    	exec sp_genMsg4Birthday_M1
			
					update ChgVipLevelHis set VipLevel=4 where Mobile='15921825165'
				
				发生日礼
				
				exec sp_genMsg4Birthday_M1
				
				exec sp_genMsg4WelcomeCoupon
				
	消费
		
		造消费数据 暂时不用这个表
		
		insert INTO TEMP_ALL_V VALUES ('13917346687', '13823285082', '小姐谈', '女', NULL, NULL, '谈', '小姐', '2018-01-04', '深圳金光华', 61, 'SZ Kingglory', 'KSS75503', '深圳金光华', 'KSS75503', N'', N'V', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00)
		
				消费金额 作废
		
		select * from TEMP_ALL_V where VIP_Mobile='13818550320'
		
				需要将交易记录的type 改为  V 
		
		UPDATE TEMP_ALL_V set Type='V'   WHERE  VIP_Mobile='13917346687'
			

删除 
	
		exec 	ll_test_shuju '17788031539'
	
		drop procedure ll_test_shuju
	
		create   procedure ll_test_shuju (@mobile VARCHAR(20))
		as
		begin
			declare @id int
			declare @usercode varchar
			declare @openid varchar
			--id,usercode,openid
			select @id=id,@usercode=usercode,@openid=openid from sysuserinfo where Mobile=@mobile;	
				if @id is not null 
						begin try	
							BEGIN tran
								SELECT @id as id;
								--删除粉丝表	
								DELETE FROM WXFans where openid=@openid;
								--删除会员主表
								DELETE FROM sysuserinfo WHERE Mobile=@mobile;
								--删除会员附表
								DELETE FROM UserAttribute WHERE userid=@id;
								--删除交易数据
								DELETE  FROM TEMP_ALL_V WHERE VIP_Mobile=@mobile;
								--删除卡券
								DELETE  from BusCoupon where openid=@openid and BusCouponCategoryId in (0,1,32,33);
								--修改领取动作
								UPDATE UserAttribute set iscoupon=0 where userid=@id;														
							commit tran
						end try
						BEGIN catch				
							ROLLBACK TRAN		
						end catch	
				else 
					return;
		end
		
		卡券	

			 修改时间，和id
			 
		update NewCustCoupon set FirstBuyTime='2019-04-20 00:00:00',
	   FirstConnState=0,SecondConnState=0,ThirdConnState=0 where id=3
		 
		 模拟
		 
		 https://wechat.katespade.aowenmarketing.com/MiniMemberCenter/Index?openid=oIH_St-CQmOXJiDIgpF92ZCZ-TYw
		 

		 select distinct u.OpenId,t.VIP_Mobile,t.VIP_Pickup_Store,t.类型,t.消费次数  from TEMP_ALL_V t join SysUserInfo u on t.VIP_Mobile = u.Mobile where  t.Type='V' and t.Birth_M='5' and openid  is null
		 
		 模板消息
		 
		select top 10 * from VIP_SalesInfo where  mobile='92115572'
		
	 select * from WXTemplateMsg where id=9 
	 
	  select * from WXTemplateMsgInfo ORDER BY id desc
		
	 需要拉取的数据
	  select  w.createtime,s.mobile from WXTemplateMsgSend w, sysuserinfo s where w.WXTemplateMsgInfoid=9 and w.createtime > '2019-07-30 23:59:00' and w.FansOpenId=s.openid order by w.id
		
		select  count(*) from WXTemplateMsgSend w, sysuserinfo s where w.WXTemplateMsgInfoid=9 and w.createtime > '2019-07-30 23:59:00' and w.FansOpenId=s.openid order by w.id
	 修改关注状态 没关注才发短信
	 
	 select  top 20 * from WXTemplateMsgSend  ORDER BY id desc    --   oUaMnwyz7oeam8mUpdLoJoig_7Xg
		
		delete from WXTemplateMsgSend where 
			 		  
		 
		 select * from WXTemplateMsgInfo where MsgId='0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI'  -- 19
		 	 
		 select  COUNT(*) from WXTemplateMsgSend  where WXTemplateMsgInfoid=9 and ProcessPlanTime  between '2019-06-01 00:00:00' and '2019-06-02 00:00:00' ORDER BY id desc  
		 
		 and fansopenid='oIH_St9ryIZQaH894yzY-CkOC9bg'  
		 
		 短信链接
		 
		 use KateSpadeWeChat
		 
		 验证码
		  select  * from SmsRecord   order by id desc
		
		 
			发送短信 首购时间
		 
			exec sp_genMsg4NewCust
		 
				发送短信
				
			     
				sp_genMsg4Birthday_M1.sql  当月1号
				sp_genMsg4Birthday_NewBind.sql  当月绑定 不是1号
				sp_genMsg4NewCust.sql   新客短信
				sp_genMsg4WelcomeCoupon.sql  欢迎礼
				UP_NewCustCoupon.sql  
				
			
			
			卡券类型
			
			select * from WXCardInfo where CardId 
			in('pUaMnwylwzcGxFMlpP9p1gF1OO9M','pUaMnw2aeX8jXNWuxFGV63W4XZ5k','wedoCardId001','wedoCardId005',--大陆
			'pUaMnw0wMK9ifQLTSvpcHZlyV5Ok','pUaMnwxw8M2g-mgv1pMknkqXkOos','wedoCardId002','wedoCardId006',--香港
			'pUaMnw6apdOHtmQmSqH8tIRYXn-M','pUaMnw9_A0ra0s74mSfriC-oM_qI','wedoCardId004','wedoCardId008',--澳门
			'pUaMnw5IPEOtHzn6BZrYaNmBk3jU','pUaMnw8qxQhGz35Nyl9kSVv-6k1Y','wedoCardId003','wedoCardId007')--台湾
		 
		 身份 
		 
		 
		 sp_genMsg4NewCust.sql
		 
		 
		 
		    交易记录
				
				select * from BusOrderDetail where SysUserInfoid=510253977     [BusProductId] >0 order by id desc
					
				INSERT INTO [BusOrderDetail]( [BusProductId], [Quantity], [Price], [Total], [TransactionTime], [WXShopId], [SysUserInfoId], [CreateId], [CreateTime], [UpdateId], [UpdateTime], [BatchNumber], [BusOrderDetailImportId], [UniqueNumber], [Remark], [DiscountAmount], [StyleSize], [ShopCode], [OrderNo], [OriginalPrice], [DiscountCode], [DiscountDesc], [Point], [PointExpiredDate]) VALUES ( 9, 1, 500.0000, 500.0000, '2019-01-09 12:58:00.000', 14, 510253977, 0, '2019-02-03 02:00:27.963', 0, '2019-02-03 02:00:27.963', N'20180130090204878', 7666431, N'KSS02110000069581', N'', 66.1100, N'', N'KSS02803', N'00006958', .0000, N'', N'', 0, NULL)

				select top 100 * from BusProduct order by id 
				
     日志
		 
		 select top 1000 * from LogApi

			order by id desc


			select top 1000 * from LogRun
			order by id desc


			select top 100 * from WXTemplateMsgSend order by id desc

			select top 100 * from SmsRecord order by id desc
		
		exec sys.sp_readerrorlog 0,1 ,'listening'
		

select SourceId,CreateTime,* from WXFans where UnionId='oVTmZ1CgEzG6Fqqz6YhemtgH6kE8'
select * from MiniFans where unionid='oVTmZ1A6OrbRmKNC7Tv9k3snTbuI'
select * from WXQRCodeLimit where WXSourceId=412
select top 100* from WXMessageRecord where FromUserName='oIH_St0_4Aj2hcqRPgOFsgmRK73E' order by id desc
select * from BusCoupon where Code='532894791981'
select * from WXCardInfo where cardid='pIH_St1LXYlZ_bejsm1XrihqNVtQ'
		
		
		