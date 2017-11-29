#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 12:35:08
# @Author  : lipeipei (2577892024@qq.com)


from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		pass

	

if __name__ == '__main__':
	app.run()
