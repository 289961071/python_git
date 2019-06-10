#!/usr/bin/python
# -*- coding:utf8 -*-
import pymssql
server1 = "localhost"
server = "192.168.1.40"
user = "lilu"
pwd = "Lilu329297!@#"
con = pymssql.connect(server, user, pwd,'katespadewechat')
# con1 = pymssql.connect('localhost', 'sa', '123456','lilu')
# 接收返回值
cuesor = con.cursor()
ziduan=['17788031539',"oUaMnwyz7oeam8mUpdLoJoig_7Xg",1]
for i in range(2):
    cuesor.execute(" select  top 1 * from WXTemplateMsgSend where WXTemplateMsgInfoid  =%s ORDER BY id desc",(i+1  ,))
    row = cuesor.fetchall()
    # for j in row:
    canshu=list(row[0])
    canshu[3]='oUaMnwyz7oeam8mUpdLoJoig_7Xg'
    canshu[6]=1
    # canshu.pop(0)
    print(canshu)

        # cuesor.execute("INSERT INTO WXTemplateMsgSend([WXTemplateMsgInfoId], [PlatformOpenId], [FansOpenId], [DataJson], [Url], [ProcessStatus], [ProcessPlanTime], [ProcessTime], [ProcessTimes], [ProcessResult], [CreateTime], [CreateId], [DataId], [MiniProgramAppid], [MiniProgramPagePath])"
        #                " VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s, %s);",tuple(canshu))
        # con.commit()
cuesor.close()
con.close()