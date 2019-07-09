#!/usr/bin/python
# coding=utf-8
# ll 雅培测试库微信
import smtplib,pymssql,pandas
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def shujuk():
    server = "192.168.1.40"
    user = "lilu"
    pwd = "Lilu329297!@#"
    con = pymssql.connect(server, user, pwd,'abbottdiabeteswechat')
    # 接收返回值
    cuesor = con.cursor()
    ziduan=[8,'2ww','sss']
    cuesor.execute("select top 50 * from logapi where apiurl like '%QueryPoint%'")
    row = cuesor.fetchall()
    # con.commit()
    #打印字段名
    ziduan=[]
    for i in  cuesor.description:
        print(i[0])
        ziduan.append(i[0])
    # print(len(cuesor.description))
    # print(ziduan)
    #循环打印出对应的数据为list
    rows=[]
    for r in  row:
        rows.append(r)
    f=pandas.DataFrame(rows,columns=ziduan)
    print('表正在打印。。')
    f.to_csv('d:/d.csv',mode='w')

def youjian():
    send = '289961071@qq.com'
    pwd = 'snjlrjiadbtxbgib'
    # sendto = ['289961071@qq.com','lilu@wedochina.cn','tanchangyi@wedochina.cn']
    sendto = [ 'lilu@wedochina.cn']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    msg1 = MIMEText('内容是：apiurl 前五十数据与附件 ...', 'plain', 'utf-8')
    msg = MIMEMultipart()

    msg['Subject'] = '主题：雅培测试数据库'
    msg['From'] = send
    msg['To'] = ','.join(sendto)
    # 添加附件
    f = MIMEText(open('D:/d.csv', 'rb').read(), 'base64', 'utf-8')
    f["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    f["Content-Disposition"] = "attachment; filename='d.csv'"
    msg.attach(f)
    msg.attach(msg1)

    sm = smtplib.SMTP_SSL('smtp.qq.com', 465)
    sm.login(send, pwd)
    sm.sendmail(send, sendto, msg.as_string())
    sm.quit()
    print('发送OK')
if __name__ == '__main__':
    shujuk()
    youjian()