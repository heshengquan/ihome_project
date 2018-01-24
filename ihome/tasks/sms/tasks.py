# coding:utf-8


from ihome.libs.yuntongxun.sms import CCP
from ihome.tasks.main import app


# 定义任务
@app.task
def send_template_sms(to, datas, temp_id):
    """发送短信"""
    ccp = CCP()
    ret = ccp.send_template_sms(to, datas, temp_id)
    return ret



