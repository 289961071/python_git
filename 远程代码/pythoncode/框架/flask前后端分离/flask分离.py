# coding=utf-8
# 李路
from flask import Flask, render_template, request, jsonify
from flask import Flask,url_for

app = Flask(__name__)
@app.route('/')
def index():
    pass
@app.route('/ll')
def index1():
    pass