创建存储过程 不支持修改alter 住能删除在create

delete from user1 where name='ll'

CREATE  PROCEDURE select_by_canshu(in a INTEGER(20))
BEGIN
	DECLARE b int DEFAULT 0;
	set b:=(SELECT count(*) as b FROM user1 WHERE id>a);
	select b;
END

show engines;
 
show create table user1
 
drop procedure if exists tt

CREATE PROCEDURE tt(in a varchar(20) )  
    BEGIN  
    DECLARE t INTEGER DEFAULT 0;
		DECLARE b INTEGER DEFAULT 0;		
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET t=1;  
		set b:=(SELECT count(*) FROM user1 WHERE name=a);
        START TRANSACTION;
					insert into user1(name,pwd) values(a,'cs3');
					
        IF t = 1 or b > 0 THEN  
            ROLLBACK;  
        ELSE 							
            COMMIT;  
        END IF;  
   select t,b;   
END

调用存储过程 有()

CALL select_by_canshu(3)

call tt('ll')

删除存储过程 没有()

drop PROCEDURE if exists select_by_canshu1

查询存储过程
		指定的存储过程 没有()
		
show create procedure select_by_canshu

   所有的存储过程
	 
show procedure status

创建触发器

CREATE TRIGGER up 
AFTER INSERT on user1
FOR each row
BEGIN
	INSERT into user2(name,pwd) VALUES('cs','cs');
END

查看触发器

SELECT * FROM information_schema.`TRIGGERS`
show triggers

指定触发器
	
SHOW CREATE TRIGGER up

删除触发器

DROP TRIGGER IF EXISTS  up


INSERT INTO user1 (name,pwd) VALUES ('lk','lk')

识图 为了保障数据安全性，提高查询效率。
创建

create  view shitu1(id,name,pwd,dada)
as 
SELECT user3.id,user3.name,user3.pwd,user1.date1 FROM user3,user1 WHERE user1.id=user3.id;
with  check option

查看全部

show table status where comment='view'

		查看指定

show create view shitu1

SELECT * FROM shitu1

删除识图

drop view 
if exists 
shitu1

修改

alter view shitu1 as

SELECT user3.id,user1.date1 FROM user3,user1 WHERE user1.id=user3.id;
