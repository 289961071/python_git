use abbott_suervy190715

select * from customer 

update Customer set mobile='' where mobile='17788031539'

--  https://abbotth5.wedochina.cn/question?useropenid=ol56vw3R6dFqT74HAUoKkfEBfkuE

select * from JoinNumber where IsAllRight>0 and openid='ow_TXjhtigzmViZ4fcBLBAj0hxoI' and EndTime>'2019-07-22'


INSERT INTO [JoinNumber]( [OpenId], [CreateTime], [IsAllRight], [EndTime], [Times]) VALUES ( N'ow_TXjvwTG88iC8et6fVLWFoicG0', '2019-07-20 14:01:55.733', '1', '2019-07-20 14:03:01.213', '00:02:30.4800000'); 

select * from RebirthCard 

--用户
select *  from Customer where  openid='ol56vwxTMwisjDZ80hx8HGqOtq1w'

update Customer set InviteCount=0, Mobile='' where openid='ol56vwyhceW-n7nlV63JktG0-dX4'

--抽奖次数 select * from JoinNumber where openid='ol56vwxTMwisjDZ80hx8HGqOtq1w'
delete from JoinNumber where openid='ol56vwxTMwisjDZ80hx8HGqOtq1w'
--奖品 select * from LotteryRecord where userid='ow_TXjswyzK39eQ9H-pK7AbWkBe8'
delete from LotteryRecord where userid='ol56vwxTMwisjDZ80hx8HGqOtq1w'
--关系表 select *from RebirthCard where CustomerOpenId='ol56vwxTMwisjDZ80hx8HGqOtq1w' or CurrOpenId='ol56vwxTMwisjDZ80hx8HGqOtq1w'
delete  from RebirthCard where CustomerOpenId='ol56vw8nqowrwRYxfzMvE6MjTCus' or CurrOpenId='ol56vw8nqowrwRYxfzMvE6MjTCus'
--答题
delete from AnswerRecord where openid='ol56vwxTMwisjDZ80hx8HGqOtq1w'

题目和答案

SELECT s.OptionName, t.id from SuervyTitle t,SuervyOption s where t.TitleName like '%夏季运动%' and t.Id=s.TitleId and s.IsRight=1

select * from SuervyTitle where TitleName like '%夏季运动%'

SELECT * from SuervyOption where TitleId=173

update SuervyOption set OptionName='饮一杯开水，防止运动过程中缺水' where optionid=518

update SuervyOption set OptionName='感觉良好时，血糖监测意义不大' where optionid=467

update SuervyOption set OptionName='实时监测血糖，多方面控制血糖' where optionid=468





