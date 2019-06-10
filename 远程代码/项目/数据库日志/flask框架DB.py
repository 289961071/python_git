#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
from flask import Flask, render_template, request, session, jsonify, url_for, redirect, Response
from xiangmu.数据库日志 import SqlServerDateBase

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = '123456'


@app.route('/login', methods=['POST', 'GET'])
def denglu():
    if (request.method == 'GET'):
        return render_template('login1.html', loginname='登录...')
    else:
        f = request.get_json()
        if f['xuanze'] == 'denglu':
            print(f['user'], f['pwd'])
            # 设置session
            session['loginsession'] = 'loginlsession'
            sql = 'EXEC select_by_canshu %s, %s'
            a = SqlServerDateBase.select_sql_canshu(sql, f['user'], f['pwd'])
            if a == 'no':
                return jsonify({'d': '账户or密码错误！'})
            elif a['tiao'] == 1:
                if a['zhi'][0][0] == 1:
                    return jsonify({'d': '账户已经登录,请注销！'})
                else:
                    print('权限是：', a['zhi'][0][0])
                    session['zhanghao'] = f['user']
                    return jsonify({'url': 'index', 'zhanghao': f['user']})

        if f['xuanze'] == 'zhuce':
            sql = 'EXEC insert_by_canshu %s,%s'
            a = SqlServerDateBase.select_sql_canshu(sql, f['user'], f['pwd'])
            if a == 'no':
                return jsonify({'d': '系统异常！'})
            elif a['zhi'][0][0] != 0:
                return jsonify({'d': '账户已被注册！'})
            else:
                session['zhanghao'] = f['user']
                return jsonify({'url': 'index', 'zhanghao': f['user']})
        if f['xuanze'] == 'zhuxiao':
            sql = 'EXEC EXEC update_by_power %s,%s'
            pass


@app.route('/shuju', methods=['POST', 'GET'])
def gai():
    if (request.method == 'GET'):
        return redirect(url_for('denglu'))
    else:
        f = request.get_json()
        print('表格查询参数', f['canshu'])
        sql2 = 'EXEC select_shuju %s'
        a = SqlServerDateBase.select_sql_canshu(sql2, f['canshu'], 'null')
        if a == 'no':
            return jsonify({'d': '账户密码错误！'})
        else:
            print(a['zhi'])
            # 经典的数据格式处理方法  牛皮
            aa = [i for i in a['zhi']]
        return jsonify({'zhi': aa, 'lie': a['lie'], 'tiao': a['tiao']})


@app.route('/index/<filename>')
def hello_world(filename):
    print(filename)
    resp = Response('服务器信息')
    # 设置 cookie
    resp.set_cookie('username', 'username:ll')
    # 根据 session  判断是否是指定的用户
    print('session:', session.get('zhanghao'))
    if filename == session.get('zhanghao'):
        return render_template('index.html', zhanghao=filename)
    else:
        return redirect(url_for('denglu'))


if __name__ == '__main__':
    app.run()
