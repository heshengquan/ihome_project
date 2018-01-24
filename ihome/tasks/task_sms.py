# -*- coding:utf-8 -*-

from celery import Celery
from ihome.libs.yuntongxun.sms import CCP

# 创建celery应用对象

app = Celery("ihome", broker="redis://127.0.0.1:6379/5")


# 定义任务
@app.task
def send_temp_sms(to, datas, temp_id):
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)
