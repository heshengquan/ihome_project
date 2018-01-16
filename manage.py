# -*- coding:utf-8 -*-
from flask_script import Manager
from ihome import create_app,db
from flask_migrate import MigrateCommand,Migrate

import redis
from flask import Flask

# 创建flask的app
app=create_app("develope")

# 创建管理工具的对象
manager=Manager(app)
Migrate(app,db)

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()


