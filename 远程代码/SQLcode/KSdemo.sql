select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile in ('13398115958')

select top 10  LastScanSourceId,CreateTime,* from WXFans where openid in ('oIH_StyRVo81WdCT8LC00mIRpi9c' ,'oIH_St_Xcz23RfqjXUCFBNOyqLkw')

select * from UserAttribute where userid=10517260
		
 delete  select * From NewCustCoupon where mobile='13238417797' 
		
select *  from BusOrderDetail where SysUserInfoid=510253982 and id>200

select * from [交易数据整合] where mobile='13238417797'
			
select * from WXCardPack where pack=22

select code,*from wxshop where code ='KSSHKG03'

select * from WXQRCodeLimit where WXShopId in (101)

update WXQRCodeLimit set WXSourceId=490 where WXShopId in (101)

select * from BusCoupon where openid='oIH_St6W8_Fo-NiSXE92hX8y7Dnk'

select b.code,s.mobile from BusCoupon b, SysUserInfo s  where s.openid=b.openid and s.mobile 
in (
'18615705957',
'18701777116',
'18737500999',
'18611824566',
'18602851769',
'18673189948',
'18702892998',
'13262285883',
'15104799429',
'18015585900',
'13398115958',
'13907167990'
)


select  id,openid,unionid,mobile,CreateDate,* from sysuserinfo where   Mobile in ('18615705957')


select openid,sourceid,LastScanSourceId ,nickname,createtime,updatetime,SubscribeTime,* from WXFans where openid='oIH_StwDfoTkC0fO1j5nKgwmJCnA'

select  w.createtime,s.mobile from WXTemplateMsgSend w, sysuserinfo s 
        where w.WXTemplateMsgInfoid=9 and w.createtime > '2019-07-30 23:59:00' 
        and w.FansOpenId=s.openid order by w.id

select DISTINCT s.Mobile,b.openid from BusCoupon b,sysuserinfo s where s.id=b.SysUserInfoId and b.sendtime>'2019-07-31' and 
b.CardCategoryName in ('新VIP生日礼券礼盒','新VIP生日礼券') 




