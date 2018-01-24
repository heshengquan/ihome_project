# coding:utf-8


from celery import Celery
# from ihome.tasks import config

app = Celery("ihome")

# app.config_from_object(config)
app.config_from_object("ihome.tasks.config")

# 让celery自己找到任务
app.autodiscover_tasks(["ihome.tasks.sms"])