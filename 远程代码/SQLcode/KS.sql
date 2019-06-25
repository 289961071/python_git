查询  katespadewechat

				粉丝表查看关注
	
		select id,openid,Nickname,unionid,CreateTime from WXFans where MemberId=510253841 openid='oIH_St97V2Ne39oQsKuvovo074c4'
		
		select *  from WXFans where  Nickname like '%张綝 Sophia%'  ---  oUaMnwyTwG43wiO-uHDMIvtE784A
		
		DELETE FROM WXFans where Nickname like 'vivo x21%'
		
		UPDATE WXFans set memberid=0 where  Nickname like '%heidi%'

				会员主表

		select  id,openid,unionid,mobile  from sysuserinfo where   Mobile='13917346687'-- oUaMnw_opPWHeP97xDJlZihj54Ek  o5Icn51jGsdCpqLlkP_7bsmzx0_M

		select * from sysuserinfo where Mobile='13917346687'  -- oUaMnwyz7oeam8mUpdLoJoig_7Xg    o5Icn51q5Dlu-aQHu0hB2UqDniFw
		
		UPDATE sysuserinfo set openid =''   where Mobile='15921825165'
		
		UPDATE WXFans set MemberId='' where MemberId=510253841
		

				会员附表  userID就是sysuserinfo 的id

		select * from UserAttribute where userid=510253914
		
					修改领取动作
			
			UPDATE UserAttribute set iscoupon=0 where userid=510253914
					
					会员等级
					
				UPDATE UserAttribute set level=0 where userid=510253921	
			
				卡券

		select * from BusCoupon where openid='oUaMnw3A4yVs9haCOTOvpwOuM-i0' and BusCouponCategoryId=0

		select * From NewCustCoupon WHERE unionid='o5Icn59sZBfXSZBKAVzSZ9yjG120'

				消费
		
		SELECT VIP_Mobile,VIP_NO,VIP_Name,Store_Code,累计消费金额,近六个月的消费金额 FROM TEMP_ALL_V WHERE VIP_Mobile='15921825165'

更新
				会员等级

		UPDATE UserAttribute SET level=3  where userid=510253851

				会员积分
		
		UPDATE UserAttribute SET point=6000  where userid=510253850
			
				生日
				
		UPDATE sysuserinfo SET birthday='2018-05-01' where Mobile='18501709609'

		
				入会时间和积分 等级
		
		UPDATE UserAttribute SET MemberStartTime='2019-03-08',point=6000 ,level=2 where userid=510253851
		
				造数据
		
		INSERT INTO [dbo].[TEMP_ALL_V]([VIP_Mobile], [VIP_NO], [VIP_Name], [VIP_Gender], [VIP_Birthday], [Birth_M], [VIP_LastName], [VIP_FirstName], [VIP_Reg_Date], 			[VIP_Reg_Store_Cn], [RegStoreId], [Store_En], [Store_Code], [VIP_Pickup_Store], [VIP_Pickup_Store_Code], [VIP_Email], [Type], [累计消费金额], [首次消费时间], [最后一次消费时间], [消费次数], [近五个月的消费金额], [最后一次消费门店], [类型], [上个月类型], [Tag], [Tag2], [Style], [VipStartTime], [MemberStartTime], [BindTime], [OutletsShopCode], [OutletsTime], [OutletsUserCode], [IsSubscript], [Recent12MonthConsumption], [Recent24MonthConsumption], [最后一次消费门店中文名称], [近六个月的消费金额]) 		VALUES (N'18516120659', N'13823285082', N'小姐谈', N'女', NULL, NULL, N'谈', N'小姐', '2018-01-04', N'深圳金光华', 61, N'SZ Kingglory', N'KSS75503', N'深圳金光华', 			N'KSS75503', N'', N'M', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00);
		
		insert INTO TEMP_ALL_V VALUES ('13917346687', '13823285082', '小姐谈', '女', NULL, NULL, '谈', '小姐', '2018-01-04', '深圳金光华', 61, 'SZ Kingglory', 'KSS75503', '深圳金光华', 'KSS75503', N'', N'V', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, '2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00)
		
				消费金额
		
		select * from TEMP_ALL_V where VIP_Mobile='13917346687'
		
				需要将交易记录的type 改为  V 
		
		UPDATE TEMP_ALL_V set Type='V'   WHERE  VIP_Mobile='13917346687'
		
				把usercode改回去
		
		UPDATE  sysuserinfo set  UserCode='KS201918012' where Mobile='18516120659'
		
			修改day1 day7 day14  没有就造数据  -- oUaMnwyz7oeam8mUpdLoJoig_7Xg    o5Icn51q5Dlu-aQHu0hB2UqDniFw
			
		select * From NewCustCoupon

		INSERT INTO [dbo].[NewCustCoupon]( [mobile], [openid], [unionid], [CouponPack], [CreateTime], [CouponState], [SendTime], [GetTime], [FirstBuyTime], [FansUpdateTime], [FirstConnState], [FirstConnTime], [SecondConnState], [SecondConnTime], [ThirdConnState], [ThirdConnTime], [MemberTime], [vip_type]) VALUES ('13917346687', 'oUaMnw3A4yVs9haCOTOvpwOuM-i0', 'o5Icn59sZBfXSZBKAVzSZ9yjG120', 1, '2019-04-01 18:25:01.623', 0, NULL, NULL, '2019-03-26 22:07:04.793', '2019-04-01 18:25:01.623', 2, '2019-04-01 18:33:06.063', 2, '2019-04-01 18:51:53.907', 2, '2019-04-01 18:37:40.733', '2019-04-01 18:25:01.623', NULL);
		
		update NewCustCoupon set FirstBuyTime='2019-06-10 00:00:00',
    FirstConnState=0,SecondConnState=0,ThirdConnState=0 where id=2

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
		 
	 select openid from sysuserinfo where Mobile='13761701167'  --  oIH_StyRVo81WdCT8LC00mIRpi9c   heidi      oIH_St-6zzHfYJLWMDdovZMj0AF4
		 
	 select * from WXTemplateMsg where id=1  
	 
	  select * from WXTemplateMsgInfo
		 
	 select  top 10 * from WXTemplateMsgSend where WXTemplateMsgInfoid  =1 ORDER BY id desc    --   oUaMnwyz7oeam8mUpdLoJoig_7Xg

			 		 
		 
		 select * from sysuserinfo where Mobile='17788031539'  --  oIH_St6BU-zLFL-3dN7lbDb_iiBg
		 
		 select * from WXTemplateMsgInfo where MsgId='0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI'  -- 19
		 
		 select * from WXTemplateMsg where template_id='0iqqydBRd5LdnxiaiLX7O233f7nFHyXgaScT77RVIcI'  
		 
		 select  COUNT(*) from WXTemplateMsgSend  where WXTemplateMsgInfoid=9 and ProcessPlanTime  between '2019-06-01 00:00:00' and '2019-06-02 00:00:00' ORDER BY id desc  
		 
		 and fansopenid='oIH_St9ryIZQaH894yzY-CkOC9bg'  
		 
		 短信链接
		 
		 select top 20 * from SmsRecord order by id desc
		 
		 select * from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As' and BusCouponCategoryId in (1,32,33)
		 
				发送短信
				
				短信内容
			
			
			卡券类型
			
			select * from WXCardInfo where CardId 
			in('pUaMnwylwzcGxFMlpP9p1gF1OO9M','pUaMnw2aeX8jXNWuxFGV63W4XZ5k','wedoCardId001','wedoCardId005',--大陆
			'pUaMnw0wMK9ifQLTSvpcHZlyV5Ok','pUaMnwxw8M2g-mgv1pMknkqXkOos','wedoCardId002','wedoCardId006',--香港
			'pUaMnw6apdOHtmQmSqH8tIRYXn-M','pUaMnw9_A0ra0s74mSfriC-oM_qI','wedoCardId004','wedoCardId008',--澳门
			'pUaMnw5IPEOtHzn6BZrYaNmBk3jU','pUaMnw8qxQhGz35Nyl9kSVv-6k1Y','wedoCardId003','wedoCardId007')--台湾
		 
		 身份 
		 
		 
		 
		 
		 
		 
		 