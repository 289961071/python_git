#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import smtplib
from email.mime.text import MIMEText

send = '196808384@qq.com'
pwd = 'mvukbrnqicticach'
sendto = ['289961071@qq.com','lilu@wedochina.cn']

def fasong(send,to,pwd):

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    msg=MIMEText('邮件内容是：Python 邮件发送测试...', 'plain', 'utf-8')

    msg['Subject'] = '邮件主题Python SMTP 邮件测试'
    msg['From'] = send
    msg['To'] = ','.join(to)

    # msg.attach(msg1)
    sm = smtplib.SMTP_SSL('smtp.qq.com',465)
    sm.set_debuglevel(1)
    print(sendto)
    sm.login(send,pwd)
    sm.sendmail(send,to,msg.as_string())
    sm.quit()
    print('发送OK')

def fasongfujian(send,to,pwd):

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    msg = MIMEText('邮件内容是：附件 邮件发送测试...', 'plain', 'utf-8')

    msg['Subject'] = '邮件主题Python SMTP 邮件测试ddd'
    msg['From'] = send
    msg['To'] = ','.join(to)

    #添加附件
    f=MIMEText(open(r'D:\b.txt','rb').read(),'base64','utf-8')
    f["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    f["Content-Disposition"] = "attachment; filename='b.txt'"
    msg.attach(f)

    sm = smtplib.SMTP_SSL('smtp.qq.com',465)
    sm.login(send,pwd)
    sm.sendmail(send,to,msg.as_string())
    sm.quit()
    print('发送OK')

fasongfujian(send,sendto,pwd)