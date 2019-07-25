use  katespadewechat

		粉丝表查看关注
	
		select id,openid,Nickname,unionid,CreateTime from WXFans where MemberId=510253841 openid='oIH_St97V2Ne39oQsKuvovo074c4'
		
		select *  from WXFans where    Nickname like '%那路逗%'  ---  oUaMnwyz7oeam8mUpdLoJoig_7Xg
		
		select openid,LastScanSourceId ,nickname from WXFans where openid='oIH_St9fs_0sUj-w4brO9GZnXHGw'
		
		select openid,LastScanSourceId ,nickname from WXFans where openid='oIH_StyRVo81WdCT8LC00mIRpi9c'
		
		
		
	 select * FROM WXFans where openid='oIH_St9fs_0sUj-w4brO9GZnXHGw'

		
		UPDATE WXFans set memberid=0 where  Nickname like '%heidi%'

		会员主表

		select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile='15921825165'  
		
		select  * from UserAttribute where userid=10517125
		
			UPDATE sysuserinfo SET birthday='1974-06-13' where  Mobile='13816102444' 
		
		select id,openid,NickName,sex,city,LastScanSourceId from WXFans where openid='oIH_St-6zzHfYJLWMDdovZMj0AF4'
		
		cs200
		
		select top 10 * from Raw_VIP_Full where vip_tel_2='13783714003'
		
			select top 10 * from Raw_VIP_Daily where vip_tel_2='13783714003'
		
		
		update sysuserinfo set activeshopcode='kss02301' where Mobile='17788031539'  
		
		-- oUaMnw_opPWHeP97xDJlZihj54Ek  o5Icn51jGsdCpqLlkP_7bsmzx0_M 10000771
	
		select  * from UserAttribute where userid='10513873'
		
		select * from BusCoupon where OpenId='oIH_StyLPrhOFvrVpWipiHrNY49g'
	
		--activityshopcode 是正价 奥莱店 WXSHOP表
		
		select * from sysuserinfo where Mobile='18017695729'  --    oUaMnw9Cg3cSrnNKTNvJWVSWw2As
		
				update sysuserinfo set activeshopcode='kss02301' where mobile='15921825165'  --  正价  kss02301   奥莱  kss02202
		
		UPDATE sysuserinfo set openid =''   where Mobile='15921825165'
		
		UPDATE WXFans set MemberId='' where MemberId=510253841
			
			查看正价还是奥莱
			
			select *from wxshop
			
			select * from BusProduct
			
			select * from WXQRCodeLimit where WXSourceId=153
			
			select * from HMTShopBindCard
			
		会员附表  userID就是sysuserinfo 的id

		select * from UserAttribute where userid=10406272
		
					修改领取动作
			
					UPDATE UserAttribute set iscoupon=0 where userid=510253914
					
					会员等级
					
					UPDATE UserAttribute set level=2 where userid=510253939	
					
					会员积分
		
					UPDATE UserAttribute SET point=6000  where userid=510253850
			
					生日
				
					UPDATE sysuserinfo SET birthday='2018-06-01' where Mobile='10086402'
					
					入会时间和积分 等级
		
					UPDATE UserAttribute SET MemberStartTime='2019-03-08',point=6000 ,level=2 where userid=510253851
			
		卡券
					select * from sysuserinfo WHERE Mobile='18017695729'   ---   oUaMnw9Cg3cSrnNKTNvJWVSWw2As

		select * from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As' 
			
					删除领取的卡券
				
				delete from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As'
					
					新客卡券
				select * From NewCustCoupon WHERE unionid='o5Icn59sZBfXSZBKAVzSZ9yjG120'
		
					对应领取的卡  couponpack  状态 0是未发送 1 已发送 2 已领取
					
				update 	NewCustCoupon set couponpack=23,CouponState=0 where mobile='15921825165'
			
				修改day1 day7 day14  没有就造数据  -- oUaMnwyz7oeam8mUpdLoJoig_7Xg    o5Icn51q5Dlu-aQHu0hB2UqDniFw
			
				select * From NewCustCoupon where mobile='18017695729'
		
				select * from ChgVipLevelHis  where mobile='' --15921825165 查看有没有手机 没有就不发短信

				INSERT INTO [dbo].[NewCustCoupon]( [mobile], [openid], [unionid], [CouponPack], [CreateTime], [CouponState], [SendTime], [GetTime], [FirstBuyTime], [FansUpdateTime], [FirstConnState], [FirstConnTime], [SecondConnState], [SecondConnTime], [ThirdConnState], [ThirdConnTime], [MemberTime], [vip_type]) VALUES ('18017695729', 'oIH_St_dMLhOLB8GNr4hrCz0asYo', 'oVTmZ1GSFpXFm2_c4VLikgXSgeZA', 1, '2019-04-01 18:25:01.623', 0, NULL, NULL, '2019-03-26 22:07:04.793', '2019-04-01 18:25:01.623', 2, '2019-04-01 18:33:06.063', 2, '2019-04-01 18:51:53.907', 2, '2019-04-01 18:37:40.733', '2019-04-01 18:25:01.623', '金卡会员');
				
				update NewCustCoupon set FirstBuyTime='2019-06-30 00:00:00',
				FirstConnState=0,SecondConnState=0,ThirdConnState=0,vip_type='金卡会员',couponpack=23,CouponState=0 where mobile='18017695729'
				
				UPDATE UserAttribute set level=3 where userid=10443336	
				select * from UserAttribute where userid=10443336	
				发新客 短信
				
				exec sp_genMsg4NewCust
				 
		生日礼  VIPDate 必须小于等于6.1 修改自己的生日为6月份  没有就insert
				
		select * from 	ChgVipLevelHis where mobile='18017695729'    -- ChgVipLevelHis VipLevel等级决定你拿什么样的生日礼
			
					INSERT INTO [ChgVipLevelHis]( [SysUserInfoId], [Mobile], [VipLevel], [VipDate], [ExpiryDate], [UpgradeType], [Points], [CreateTime], [Remark]) VALUES ( 10443336, 		N'18017695729', 3, '2019-07-01', '2019-08-01', N'routine', 9999, '2019-06-25 00:00:00.000', N'手工测试');
					
				UPDATE sysuserinfo SET birthday='2018-07-01',activeshopcode='kss02301' where Mobile='18017695729'
				
    	exec sp_genMsg4Birthday_M1
			
					update ChgVipLevelHis set VipLevel=4 where Mobile='15921825165'
				
				发生日礼
				
				exec sp_genMsg4Birthday_M1
				
				exec sp_genMsg4WelcomeCoupon
				
	消费
		
		SELECT VIP_Mobile,VIP_NO,VIP_Name,Store_Code,累计消费金额,近六个月的消费金额 FROM TEMP_ALL_V WHERE VIP_Mobile='15921825165'			
		
		造消费数据
		
		INSERT INTO [dbo].[TEMP_ALL_V]([VIP_Mobile], [VIP_NO], [VIP_Name], [VIP_Gender], [VIP_Birthday], [Birth_M], [VIP_LastName], [VIP_FirstName], [VIP_Reg_Date], 			[VIP_Reg_Store_Cn], [RegStoreId], [Store_En], [Store_Code], [VIP_Pickup_Store], [VIP_Pickup_Store_Code], [VIP_Email], [Type], [累计消费金额], [首次消费时间], [最后一次消费时间], [消费次数], [近五个月的消费金额], [最后一次消费门店], [类型], [上个月类型], [Tag], [Tag2], [Style], [VipStartTime], [MemberStartTime], [BindTime], [OutletsShopCode], [OutletsTime], [OutletsUserCode], [IsSubscript], [Recent12MonthConsumption], [Recent24MonthConsumption], [最后一次消费门店中文名称], [近六个月的消费金额]) 		VALUES (N'18516120659', N'13823285082', N'小姐谈', N'女', NULL, NULL, N'谈', N'小姐', '2018-01-04', N'深圳金光华', 61, N'SZ Kingglory', N'KSS75503', N'深圳金光华', 			N'KSS75503', N'', N'M', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00);
		
		insert INTO TEMP_ALL_V VALUES ('13917346687', '13823285082', '小姐谈', '女', NULL, NULL, '谈', '小姐', '2018-01-04', '深圳金光华', 61, 'SZ Kingglory', 'KSS75503', '深圳金光华', 'KSS75503', N'', N'V', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00)
		
				消费金额
		
		select * from TEMP_ALL_V where VIP_Mobile='13917346687'
		
				需要将交易记录的type 改为  V 
		
		UPDATE TEMP_ALL_V set Type='V'   WHERE  VIP_Mobile='13917346687'
		
				把usercode改回去
		
		UPDATE  sysuserinfo set  UserCode='KS201918012' where Mobile='18516120659'
		
			

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
		
		
		
		添加交易记录 vip 生日 
		
	exec 	ll_test_shuju '17788031539'
	
	drop procedure ll_test_shuju
	
		create   procedure ll_test_shuju (@mobile VARCHAR(20))
		as
		begin
			declare @id int
			select @id=id from sysuserinfo where Mobile=@mobile;	
				if @id is not null 
						begin try	
							BEGIN tran
								SELECT @id as id;
								insert INTO TEMP_ALL_V VALUES (@mobile, '13823285082', '小姐谈', '女', NULL, NULL, '谈', '小姐', '2018-01-04', '深圳金光华', 61, 'SZ Kingglory', 'KSS75503', '深圳金光华', 'KSS75503', N'', N'M', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00)	;
								UPDATE UserAttribute SET point=6000 ,level=3 where userid=@id;
								UPDATE sysuserinfo SET birthday='2018-05-01' where Mobile=@mobile;
								UPDATE TEMP_ALL_V set Type='V'  WHERE  VIP_Mobile=@mobile;
							commit tran
						end try
						BEGIN catch				
							ROLLBACK TRAN		
						end catch	
				else 
					return;
		end
	
	发模板消息
		
		insert [NewCustCoupon]([mobile]
      ,[openid]
      ,[unionid]
      ,[CouponPack]
      ,[CreateTime]
      ,[CouponState]
      ,[SendTime]
      ,[GetTime]
      ,[FirstBuyTime]
      ,[FansUpdateTime]
      ,[FirstConnState]
      ,[FirstConnTime]
      ,[SecondConnState]
      ,[SecondConnTime]
      ,[ThirdConnState]
      ,[ThirdConnTime]
      ,[MemberTime]
	  ,vip_type
	  )
select '15921825165','oUaMnw9Cg3cSrnNKTNvJWVSWw2As','o5Icn53_345jonxOquInCfjg1ROc',1,GETDATE(),
       0,null,null,GETDATE(),getdate(),0,null,0,null,0,null,GETDATE(),null
		
select * from NewCustCoupon

			 修改时间，和id
			 
		update NewCustCoupon set FirstBuyTime='2019-04-20 00:00:00',
	   FirstConnState=0,SecondConnState=0,ThirdConnState=0 where id=3
		 
		 模拟
		 
		 https://wechat.katespade.aowenmarketing.com/MiniMemberCenter/Index?openid=oIH_St-CQmOXJiDIgpF92ZCZ-TYw
		 
		 
		 select distinct u.OpenId,t.VIP_Mobile,t.VIP_Pickup_Store,t.类型,t.消费次数  from TEMP_ALL_V t join SysUserInfo u on t.VIP_Mobile = u.Mobile where  t.Type='V' and t.Birth_M='5' and openid  is null
		 
		 模板消息
		 
	 select openid from sysuserinfo where Mobile='15921825165'  --  oIH_StyRVo81WdCT8LC00mIRpi9c   heidi      oIH_St-6zzHfYJLWMDdovZMj0AF4
		 
	 select * from WXTemplateMsg where id=1  
	 
	  select * from WXTemplateMsgInfo
	 
	 修改关注状态 没关注才发短信
	 
	 select *  from WXFans where    Nickname like '%Heidi%'
	 
	 update WXFans set subscribe=0 where Nickname like '%那路逗%'
	 
	 
	 
	 select  top 20 * from WXTemplateMsgSend  ORDER BY id desc    --   oUaMnwyz7oeam8mUpdLoJoig_7Xg
		
		delete from WXTemplateMsgSend where 
			 		 
		 
		 select * from sysuserinfo where Mobile='17788031539'  --  oIH_St6BU-zLFL-3dN7lbDb_iiBg
		 
		 select * from WXTemplateMsgInfo where MsgId='0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI'  -- 19
		 
		 select * from WXTemplateMsg where template_id='0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI'  
		 
		 select  COUNT(*) from WXTemplateMsgSend  where WXTemplateMsgInfoid=9 and ProcessPlanTime  between '2019-06-01 00:00:00' and '2019-06-02 00:00:00' ORDER BY id desc  
		 
		 and fansopenid='oIH_St9ryIZQaH894yzY-CkOC9bg'  
		 
		 短信链接
		 
		 use KateSpadeWeChat
		 
		 select top 20 * from SmsRecord  order by id desc
		 
		  select  * from SmsRecord where mobile='17788031539'  order by id desc
			
			delete from SmsRecord where   mobile in ('15921825165' ,'17788031539')
			
			select * from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As' and BusCouponCategoryId in (1,32,33)
		 
			发送短信 首购时间
		 
			exec sp_genMsg4NewCust
		 
				发送短信
				
			     
				sp_genMsg4Birthday_M1.sql  当月1号
				sp_genMsg4Birthday_NewBind.sql  当月绑定 不是1号
				sp_genMsg4NewCust.sql   新客短信
				sp_genMsg4WelcomeCoupon.sql  欢迎礼
				UP_NewCustCoupon.sql  
				
				短信内容
			
			
			卡券类型
			
			select * from WXCardInfo where CardId 
			in('pUaMnwylwzcGxFMlpP9p1gF1OO9M','pUaMnw2aeX8jXNWuxFGV63W4XZ5k','wedoCardId001','wedoCardId005',--大陆
			'pUaMnw0wMK9ifQLTSvpcHZlyV5Ok','pUaMnwxw8M2g-mgv1pMknkqXkOos','wedoCardId002','wedoCardId006',--香港
			'pUaMnw6apdOHtmQmSqH8tIRYXn-M','pUaMnw9_A0ra0s74mSfriC-oM_qI','wedoCardId004','wedoCardId008',--澳门
			'pUaMnw5IPEOtHzn6BZrYaNmBk3jU','pUaMnw8qxQhGz35Nyl9kSVv-6k1Y','wedoCardId003','wedoCardId007')--台湾
		 
		 身份 
		 
		 
		 sp_genMsg4NewCust.sql
		 
		 
		 
		    交易记录
				
				select top 100 *from BusOrderDetail where SysUserInfoid=510253977     [BusProductId] >0 order by id desc
				
					select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile='18501709317'   '15921825165'  
					update UserAttribute set LEVEL=2 where userid=510253977
					
				INSERT INTO [BusOrderDetail]( [BusProductId], [Quantity], [Price], [Total], [TransactionTime], [WXShopId], [SysUserInfoId], [CreateId], [CreateTime], [UpdateId], [UpdateTime], [BatchNumber], [BusOrderDetailImportId], [UniqueNumber], [Remark], [DiscountAmount], [StyleSize], [ShopCode], [OrderNo], [OriginalPrice], [DiscountCode], [DiscountDesc], [Point], [PointExpiredDate]) VALUES ( 9, 1, 500.0000, 500.0000, '2019-01-09 12:58:00.000', 14, 510253977, 0, '2019-02-03 02:00:27.963', 0, '2019-02-03 02:00:27.963', N'20180130090204878', 7666431, N'KSS02110000069581', N'', 66.1100, N'', N'KSS02803', N'00006958', .0000, N'', N'', 0, NULL);

				select * from WXShop  where code='KSS01010'  order by id 
				
				select top 100 * from BusProduct order by id 
				
				select top 100 * from BusOrderDetail ORDER BY id desc
				
				select * from SysUserInfo where mobile='17780515110'
				
				 # 删除所有卡券
     DELETE from BusCoupon where openid='oIH_StyRVo81WdCT8LC00mIRpi9c'
    # 删除短信 因为短信不回重复发
    "DELETE select * from SmsRecord where mobile='17788031539'
    # 删除交易数据
  
    # "DELETE  from WXFans where  OpenId='oIH_StyRVo81WdCT8LC00mIRpi9c'
    # 删除会员附表
    DELETE  FROM UserAttribute  WHERE userid='10510503'
		 select * BusCoupon where
    delete select * from sysuserinfo where  Mobile='17788031539'
		
		UPDATE sysuserinfo SET birthday='1900-07-30' where  Mobile='15755195280' 
		
		select * from wxfans where openid='oIH_St0_4Aj2hcqRPgOFsgmRK73E'
		
		select  id,openid,unionid,mobile,* from sysuserinfo where  Mobile='15755195280'    
			
		select  * from UserAttribute where userid='10301074'
		
		select * from BusCoupon where SysUserInfoId='10424197'         
		
		exec sys.sp_readerrorlog 0,1 ,'listening'
		
select BindTime,UnionId,openid,* from SysUserInfo where mobile='18606501939'
select SourceId,CreateTime,* from WXFans where unionid='oVTmZ1A6OrbRmKNC7Tv9k3snTbuI'
select * from MiniFans where unionid='oVTmZ1A6OrbRmKNC7Tv9k3snTbuI'
select * from WXQRCodeLimit where WXSourceId=412
select top 100* from WXMessageRecord where FromUserName='oIH_St0_4Aj2hcqRPgOFsgmRK73E' order by id desc
select * from BusCoupon where Code='532894791981'
select * from WXCardInfo where cardid='pIH_St1LXYlZ_bejsm1XrihqNVtQ'
		
		select top 100 * from [BusOrderDetail] where DiscountAmount<0 order by id desc
		
		select *from BusCoupon
		
		