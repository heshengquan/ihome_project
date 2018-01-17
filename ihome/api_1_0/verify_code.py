# -*- coding:utf-8 -*-
from . import api
from ihome.utils.captcha.captcha import captcha
from ihome.utils.response_code import RET,error_map
from flask import jsonify, make_response,current_app
from ihome import redis_store, constants


# url: /api/v1_0/image_codes/<image_code_id>
#
# methods: get
#
# 传入参数：
#
# 返回值： 正常：图片  异常 json


@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """提供图片验证码"""
    # 业务处理
    # 生成验证码图片
    # 名字, 验证码真实值，图片的二进制内容
    name, text, image_data = captcha.generate_captcha()

    try:
        # 保存验证码的真实值与编号
        # redis_store.set("image_code_%s" % image_code_id, text)
        # redis_store.expires("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
        # 设置redis的数据与有效期
        redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 在日志中记录异常
        current_app.logger.error(e)
        resp = {
            "errno": RET.DBERR,
            # "errmsg": "save image code failed"
            "errmsg": "保存验证码失败"
        }
        return jsonify(resp)

    # 返回验证码图片
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp
