创建存储过程

use lilu

delete from user_log

drop table user_log1

select * into user_log1 from user_log where 1<>1

		登录

CREATE / alter PROCEDURE select_by_canshu( @a VARCHAR(20), @b VARCHAR(20))
AS
BEGIN 
	declare @p int	
	--查看登录状态 上锁 禁止修改
	SELECT @p=power FROM user_login with (updlock,rowlock) WHERE zhanghao=@a AND pwd=@b;
	SELECT @p as p;
	
	if @p !=1
		--登录成功 修改状态  添加日志 try catch 加事务 tran
		begin
			begin try
				begin tran
					UPDATE user_login set power=1 where zhanghao=@a AND pwd=@b;
					insert into user_log(zhanghao,power) VALUES(@a,1); 
				commit tran
			end try
			begin catch
				rollback tran
			end catch
		end
	ELSE
		return;
end

exec select_by_canshu 'll','ll'

			下线  2权限 日志
			
CREATE / alter PROCEDURE update_by_power( @a VARCHAR(20), @b VARCHAR(20))
AS
begin	
declare @p int
SELECT @p=count(*) FROM user_login with(updlock,rowlock)  WHERE zhanghao=@a AND pwd=@b and power=1;
SELECT @p as p;
	if @p =1
			begin try	
				BEGIN tran
					select @p;
					UPDATE user_login set power=0 WHERE zhanghao=@a AND pwd=@b and power=1;	
					insert into user_log(zhanghao,power) VALUES(@a,0);				
				commit tran
			end try
			BEGIN catch				
				ROLLBACK TRAN		
			end catch	
	else 
		return;
end

EXEC update_by_power '11','11'

exec cs 'll','ll'

create alter procedure cs( @a VARCHAR(20), @b VARCHAR(20))
as
begin
	declare @p VARCHAR(20)
	SELECT @p=zhanghao FROM user_login with (updlock,rowlock) WHERE zhanghao=@a AND pwd=@b and power=1;	
	if @p is not null
		SELECT @p;
	
end
			注册 日志
			
CREATE / alter PROCEDURE insert_by_canshu( @a VARCHAR(20), @b VARCHAR(20))
AS
BEGIN
	declare @p int
	--查看是否账户存在
	SELECT @p=count(*) FROM user_login with (updlock,rowlock) WHERE zhanghao=@a ;
	SELECT @p as p;

		if @p=0
		--不存在 注册  添加日志 try catch 加事务 tran
			begin
				begin try
					begin tran
						insert into user_login(zhanghao,pwd) VALUES(@a,@b);
						insert into user_log(zhanghao,power) VALUES(@a,2);					
					commit tran
				end try
				begin catch				
					rollback tran
				end catch
		end
	ELSE
		return
END

exec insert_by_canshu '张三','dasd'

insert into user_login(zhanghao,pwd) VALUES('张三','dasd');

	查看数据
	
create / alter procedure select_shuju(@a int)
as
begin
	--牛皮的处理时间方式 SqlServer自带
	SELECT id,xiangmu,zhanghao,mima,dizhi, CONVERT(varchar(100),riqi, 120) as riqi,beizhu  from user_tb  with (UPDLOCK) where id < @a;
end

调用存储过程

EXEC select_shuju 3


exec select_by_canshu '222','22'

EXEC insert_by_canshu '李路','123'

删除存储过程 没有()

drop PROCEDURE demo1,demo2

查询存储过程

		指定的存储过程 没有()
		
sp_helptext demo2

   所有的存储过程
	 
select * from sysobjects where xtype='P'



触发器

创建
			删除账户 自动清除日志
			
CREATE / alter TRIGGER rizhi_qingchu
on user_login
after DELETE
AS
begin
	declare @zh VARCHAR(50)
	SELECT @zh=deleted.zhanghao  from deleted with(rowlock,updlock)
	begin try
		begin tran
			DELETE from user_log where user_log.zhanghao=@zh
		commit tran
	end try	
	begin catch
		rollback
	end catch
end
		
DELETE FROM user_login where zhanghao='测试2'

	日志数到50  自动清除日志
			
CREATE / alter TRIGGER rizhi_zd_qingchu
on user_login
after insert
AS
begin
	declare @zh VARCHAR(50)
	SELECT @zh=count(*)  from user_log with(rowlock,updlock)  
	if @zh>50
		begin try
			begin tran
				DELETE from user_log 
			commit tran
		end try	
		begin catch
			rollback
		end catch
end
		
DELETE FROM user_login where zhanghao='测试2'
		
		更新 临时表 deleted 旧 inserted 新
		
create / alter trigger rizhi_gengxin
on user_login
after update
as
begin
	declare @old VARCHAR(50),@new varchar(50)
	SELECT @old=deleted.zhanghao,@new=inserted.zhanghao  from deleted,inserted with(rowlock,updlock)
	begin try
		begin tran
			UPDATE user_log set zhanghao=@new where zhanghao=@old
		commit tran
	end try	
	begin catch
		rollback
	end catch
end

UPDATE user_login set zhanghao='李路' where zhanghao='张三'

	查看数据库已有触发器
	
select * from sysobjects where xtype='TR'

查看指定触发器

exec sp_helptext  up

删除

drop trigger rizhi_zhuce

drop table if exists user2 , user3 , user1


视图 
创建

create view shitu1(id,name,pwd)
as
select id,name,pwd from user1 where id <4

查看

exec sp_helptext shitu1

修改

alter view shitu1
as
select *  from user1 

删除

drop view shitu1

drop table user4

使用

SELECT * FROM shitu1

复制
select * into user3 from user1 where 1<>1

SELECT  * from user_tb  with (UPDLOCK) where id < 10  ;

BEGIN try
	BEGIN TRAN 
	insert into user_login(id,zhanghao,pwd,power)  values(8,'测试2','测试2',2);
	commit tran
end try
BEGIN catch
	ROLLBACK TRAN
end catch

临时表  全局临时表创建方式就是把上面的一个#改为两个#就可以了哈~

select *into #ok from user_log

select * from #ok

