#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
from flask import Flask, render_template, request, session, jsonify,url_for,redirect,Response
from 项目.KS import datebase,MYSQLdatebase

app = Flask(__name__)
app.secret_key = '123456'

def chaxunchuli(a):
    if a == 'no':
        return jsonify({'d': '查询结果为空！'})
    else:
        print(a['r'])
        aa = []
        for j in range(len(a['r'])):
            aa.append([str(i) for i in a['r'][j]])
        print(aa)
        return jsonify({'r': aa, 'c': a['c'], 'dd': a['d'], 'd': '共计：' + str(a['d']) + ' 条数据'})
@app.route('/login',methods=['POST', 'GET'])
def denglu():
    if (request.method == 'GET'):
        return render_template('demo3.html', name3='登录...')
    else:
        f = request.get_json()
        if f['xuanze']=='denglu':
            print(f['user'],f['pwd'])
            #设置session
            session['loginsession']='loginlsession'
            sql3='CALL select_by_canshu( %s, %s)'
            sql2='UPDATE user1 SET num=1 WHERE name= %s and pwd= %s'
            a=MYSQLdatebase.select_sql_canshu(sql3,f['user'],f['pwd'])
            if a=='no':
                return jsonify({'d': '账户or密码错误！'})
            else:
                b = MYSQLdatebase.gai_sql_canshu(sql2, f['user'],f['pwd'])
                if b=='no':
                    return jsonify({'d': '账户已经登录！'})
                else:
                    return jsonify({'r':'index', 'c': f['user']})
        if f['xuanze']=='zhuce':
            sql = 'INSERT into  user1(name,pwd) VALUES (%s,%s)'
            a = MYSQLdatebase.select_sql_canshu(sql, f['user'], f['pwd'])
            if a == 'no':
                pass

@app.route('/gai', methods=['POST', 'GET'])
def gai():
    if (request.method == 'GET'):
        print(url_for('hello_world',f='ll'))
        return render_template('demo2.html', name2='xiugai')
    else:
        f = request.get_json()
        print(f['xuanze'])
        print(f['canshu'])
        if f['xuanze']=='':
            return redirect(url_for('hello_world',f='aaa'))
        else:
            return jsonify({'r':'index', 'c': f['xuanze']})
        # return 'succes'
        # sql2='DELETE FROM TEMP_ALL_V WHERE VIP_Mobile= %s'
        # sql2='DELETE FROM TEMP_ALL_V WHERE VIP_Mobile= %s'
        # if f['xuanze'] == 'zengjia':
        #     a = datebase.insert_shouji(f['canshu'])
        #     if a == 'no':
        #         return jsonify({'d': '增加失败！'})
        #     else:
        #         return jsonify({'d': '增加成功！'})
        #
        # if f['xuanze'] == 'shanchu':
        #     a = datebase.upde_sql_canshu(sql2,f['canshu'])
        #     if a == 'no':
        #         return jsonify({'d': '删除失败！'})
        #     else:
        #         return jsonify({'d': '删除成功！'})
        #
        # if f['xuanze'] == 'gengxin':
        #     return jsonify({'d': '暂时未此完善方法！'})

@app.route('/cha', methods=['POST', 'GET'])
def cha():
    if (request.method == 'GET'):
        return render_template('demo1.html', name1='chaxun')
    else:
        session['name2'] = '传过来的(查询)结果_sesssion'
        sql1="select id,name,UserCode,sex,birthday,Mobile, unionid from sysuserinfo " \
            "where Mobile like %s "
        sql2="select id,openid,Nickname,unionid,CreateTime from WXFans where Nickname like %s"
        sql3="SELECT VIP_Mobile,VIP_NO,VIP_Name,Store_Code,累计消费金额,近六个月的消费金额 "\
                       "FROM TEMP_ALL_V WHERE VIP_Mobile LIKE %s"
        f = request.get_json()
        print(f['xuanze'],f['canshu'])

        if f['xuanze'] == 'shouji':
            a = datebase.select_sql_canshu(sql1,f['canshu'])
            return chaxunchuli(a)

        if f['xuanze'] == 'nicheng':
            a = datebase.select_sql_canshu(sql2,f['canshu'])
            return chaxunchuli(a)

        if f['xuanze'] == 'xiaofei':
            a = datebase.select_sql_canshu(sql3,f['canshu'])
            return chaxunchuli(a)

@app.route('/index/<filename>')
def hello_world(filename):
    print(filename)
    sql = 'SELECT * FROM `user1` WHERE name= %s AND num= %s '
    a = MYSQLdatebase.select_sql_canshu(sql,filename, 1)
    if a=='no':
        return redirect(url_for('denglu'))
    else:
        resp=Response('服务器信息')
        #设置 cookie
        resp.set_cookie('username','username:ll')
        #设置 session
        session['denglu'] = 'denglu_sesssion'
        return render_template('index3.html', name1=filename)
@app.route('/likai/<filename>')
def likai(filename):
    print(filename)
    sql = 'UPDATE user1 SET num=0 WHERE name= %s '
    a = MYSQLdatebase.gai_sql_canshu(sql,filename, 1)
    if a == 'no':
        return jsonify({'d': '注销失败,重试！'})
    else:
        return jsonify({'d': '注销ok,请登录！'})

if __name__ == '__main__':
    app.run()

