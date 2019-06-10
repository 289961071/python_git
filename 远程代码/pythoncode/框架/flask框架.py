#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
from flask import Flask, render_template, request, session, jsonify
from 框架 import datebase

app = Flask(__name__)
app.secret_key='123456'


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ll/<aname>')
def hello_world1(aname):
    return render_template('index3.html',name1=aname + '_sama')

@app.route('/ll')
def hello_world2():
    return render_template('index3.html', name1='上线咩')

@app.route('/upload', methods=['post', 'get'])
def hello_world3():
    if (request.method == 'GET'):
        return render_template('bbb.html', name='李路大人')
    else:
        session['name2'] = '_sama_sesssion'
        print('传值OK')
        f = request.form
        print(f['pwd'],f['name'])
        a = datebase.shujuku(f['name'], f['pwd'])
        if a == 'ok':
            return jsonify({'login': '登录ok', 'name': f['name'], 'pwd': f['pwd']})
        else:
            return jsonify({'login': '登录no', 'name': f['name'], 'pwd': f['pwd']})


if __name__ == '__main__':
    app.run()
