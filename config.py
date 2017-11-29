#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-08 09:42:23
# @Author  : lipeipei (2577892024@qq.com)
# @Link    : www.baidu.com
# @Version : $Id$
'''
配置信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

'''
import os

DEBUG = True

SELECT_KEY = os.urandom(24)

DIALECT='mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa'
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
DB_URI=SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True







