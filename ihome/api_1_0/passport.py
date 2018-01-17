# coding:utf-8

import re
from . import api
from flask import request, jsonify, current_app, session
from ihome.utils.response_code import RET
from ihome import redis_store, db
from ihome.models import User


# POST /api/v1_0/users
@api.route("/users", methods=["POST"])
def register():
    """用户注册"""
    # 接受参数, 手机号、短信验证码、密码, json格式的数据
    # json.loads(request.data)
    # request.get_json方法能够帮助将请求体的json数据转换为字典
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")

    # 校验参数
    if not all([mobile, sms_code, password]):
        resp = {
            "errno": RET.PARAMERR,
            "errmsg": "参数不完整"
        }
        return jsonify(resp)

    # 判断手机号格式
    if not re.match(r"1[34578]\d{9}", mobile):
        resp = {
            "errno": RET.DATAERR,
            "errmsg": "手机号格式错误"
        }
        return jsonify(resp)

    # 业务逻辑
    # 获取真实的短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        resp = {
            "errno": RET.DBERR,
            "errmsg": "查询短信验证码错误"
        }
        return jsonify(resp)

    # 判断短信验证码是否过期
    if real_sms_code is None:
        resp = {
            "errno": RET.NODATA,
            "errmsg": "短信验证码过期"
        }
        return jsonify(resp)

    # 对于用户输入的短信验证码是否正确
    if real_sms_code != sms_code:
        resp = {
            "errno": RET.DATAERR,
            "errmsg": "短信验证码错误"
        }
        return jsonify(resp)

    # 删除短信验证码
    try:
        redis_store.delete("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 判断手机号是否注册
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     resp = {
    #         "errno": RET.DBERR,
    #         "errmsg": "数据库异常"
    #     }
    #     return jsonify(resp)
    #
    # if user is not None:
    #     # 表示已经注册过
    #     resp = {
    #         "errno": RET.DATAEXIST,
    #         "errmsg": "用户手机号已经注册"
    #     }
    #     return jsonify(resp)

    # 保存用户的数据到数据库中










