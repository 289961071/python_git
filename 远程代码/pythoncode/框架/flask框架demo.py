#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
from flask import Flask, render_template, request, session, jsonify, make_response, Response

app = Flask(__name__)
app.secret_key = '123456'


# os.urandom(24)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ll')
def hello_world2():
    # Response.set_cookie(key='cook1', value='cook111',max_age=3600)
    return render_template('demo1.html', name1='mie')


@app.route('/ll/log', methods=['POST', 'GET'])
def hello_world3():
    if (request.method == 'GET'):
        return render_template('demo1.html', name1='访问错误')
    else:
        print(session.get('name2'))
        print(request.cookies)
        f = request.get_json()
        print(f['mz'], f['pwd'])
        session['name2'] = '_ajax_sesssion'
        session['name1'] = '_ajax1111_sesssion'
        print('传值OK')

        return jsonify({'login': '登录ok', 'xinxi': f['mz'] + ':' + f['pwd'], 'session1': session['name1']})


if __name__ == '__main__':
    app.run()
