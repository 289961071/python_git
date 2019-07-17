select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile in ('19992131139')

select top 10  LastScanSourceId,CreateTime,* from WXFans where openid in ('oIH_StyRVo81WdCT8LC00mIRpi9c' ,'oIH_St_Xcz23RfqjXUCFBNOyqLkw')

select * from UserAttribute where userid=10517260
		
select * From NewCustCoupon where mobile='13238417797'
		
select * from BusOrderDetail where SysUserInfoid=10517260

select * from [交易数据整合] where mobile='13238417797'
			
select * from WXCardPack where pack=22

select code,*from wxshop where code ='KSSHKG03'

select * from WXQRCodeLimit where WXShopId in (101)

update WXQRCodeLimit set WXSourceId=490 where WXShopId in (101)

select * from BusCoupon where openid='oUaMnw9Cg3cSrnNKTNvJWVSWw2As' 