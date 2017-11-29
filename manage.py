#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 12:42:43
# @Author  : lipeipei (2577892024@qq.com)

from flask_script import Manager
from zlktqa import app
from flask_migrate import Migrate,MigrateCommand
from exts import db

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app,db)

# 添加迁移脚本的命令到manage中
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
	manager.run()
