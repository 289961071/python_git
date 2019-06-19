查询 
SELECT * FROM CRMUser WHERE  UnionId IS NOT NULL
 
SELECT * FROM CRMUser WHERE  StoreCode IS  NULL

SELECT * FROM CRMUser WHERE  Mobile IN ('17788031539') OR Mobile LIKE '185%'

SELECT * FROM user1 WHERE id BETWEEN 2 and 3
 
SELECT * FROM user1,user2 WHERE  user1.id=user2.id

SELECT * FROM user1,user2,user3 WHERE  user1.id=user2.id and user1.id=user3.id

SELECT DISTINCT name FROM user1 ORDER BY name

SELECT DISTINCT name FROM user1 ORDER BY name DESC

SELECT count(id) FROM user1 WHERE id IN(1,2,3,4)

SELECT name,sum(num) FROM user1  GROUP BY name

SELECT NOW() FROM user1

复制表 不要数据 1<>1 要数据不加条件

select  * into user_log1  from user_log where 1<>1

判断存在mysql
SELECT TABLE_NAME FROM information_schema.TABLES WHERE  TABLE_NAME='Logapi' AND table_schema='AbbottDiabetesWeChat'

SELECT count(*) FROM sys.TABLEs WHERE name='user1'

切换数据库
USE lilu

插入

INSERT INTO user_tb(xiangmu,zhanghao,mima,dizhi,beizhu) VALUES
('腾讯邮箱','lilu@wedochina.cn','Qaz123','https://exmail.qq.com/cgi-bin/loginpage',null),
('OA系统','lilu1','123456','http://oa.wedochina.cn:8090/main/login.jsp',null),
('GitLab','lilu@wedochina.cn','qq123456','http://192.168.1.51/abbott/mgm2019.git',null),
('GitHub','289961071','qq123456+.','https://github.com/',null),
('正式雅培库','lilu','Lilu329297!@#','ali-rds-01-o.sqlserver.rds.aliyuncs.com,3433','数据库名称：abbottdiabeteswechat'),
('测试库','lilu','Lilu329297!@#','192.168.1.40,1433','目前所有的测试库'),
('雅培测试后台','abbottdev\Azureadmin','Crmadmin123$%^','abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn','删除用户'),
('路虎捷豹测试后台','admin','123','jladmin.wedochina.cn/admin.php ','数据管理')

更新
UPDATE user1 SET name='李路' WHERE id =4

删除数据 不加条件全部删除

DELETE FROM user1 WHERE id = 8

delete from user_log1

创建表

CREATE TABLE user_tb(
id int identity(1,1) primary key,
xiangmu  VARCHAR(255) not null,
zhanghao VARCHAR(255),
mima VARCHAR(255),
dizhi VARCHAR(255),
riqi datetime DEFAULT getdate(),
beizhu VARCHAR(255)
)


create table user_log (
id int identity(1,1) primary key,
zhanghao VARCHAR(255) not null,
riqi datetime DEFAULT getdate(),
caozuo VARCHAR(255)
)

删除表

DROP TABLE if exists user3,user_tb

创建数据库
CREATE DATABASE lilu2

use lilu2 

	CREATE  TABLE user2(
	id int,
	name VARCHAR(255),
	pwd VARCHAR(255),
	num INT(20) DEFAULT 0
	)
	
删除数据库

DROP DATABASE lilu2


Select CONVERT(varchar(100), GETDATE(), 120)
	
	函数   SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。NOW() 返回当前时间


	SELECT name, SUM(pwd),NOW() FROM user1 GROUP BY name HAVING SUM(pwd)
	
	select count(name) from user1
	
	去重后的个数
	
	select count(distinct name) from user1
	
	UCASE 函数把字段的值转换为大写。LCASE 函数把字段的值转换为小写。
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	