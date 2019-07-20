select  id,openid,unionid,mobile,* from sysuserinfo where   Mobile in ('13689088344')

select top 10  LastScanSourceId,CreateTime,* from WXFans where openid in ('oIH_StyRVo81WdCT8LC00mIRpi9c' ,'oIH_St_Xcz23RfqjXUCFBNOyqLkw')

select * from UserAttribute where userid=10517260
		
select * From NewCustCoupon where mobile='13238417797'
		
select * from BusOrderDetail where SysUserInfoid=10517260

select * from [交易数据整合] where mobile='13238417797'
			
select * from WXCardPack where pack=22

select code,*from wxshop where code ='KSSHKG03'

select * from WXQRCodeLimit where WXShopId in (101)

update WXQRCodeLimit set WXSourceId=490 where WXShopId in (101)

select * from BusCoupon where openid='oIH_St6W8_Fo-NiSXE92hX8y7Dnk'

select b.code,s.mobile from BusCoupon b, SysUserInfo s  where s.openid=b.openid and s.mobile 
in (
'13418111510',
'13928872228',
'18520686885',
'15800611598',
'15995550024',
'18701777116',
'18516356534',
'15802138818',
'13917993180',
'13831099688',
'15080743632',
'18737500999',
'13689088344',
'13689088344',
'15011518150',
'18737500999',
'18615705957',
'13512295359',
'18601984501',
'15122253611',
'13685878878',
'15650709450',
'18611824566'
)