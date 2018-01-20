# coding:utf-8

from . import api
from ihome.utils.commons import login_required
from flask import g, request, jsonify, current_app
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.models import User
from ihome import constants


@api.route("/users/avatar", methods=["POST"])
@login_required
def set_user_avatar():
    """设置用户头像"""
    # 获取参数, 头像图片、用户
    user_id = g.user_id
    image_file = request.files.get("avatar")

    # 校验参数
    if image_file is None:
        # 表示用户没有上传头像
        return jsonify(errno=RET.PARAMERR, errmsg="未上传头像")

    # 保存用户头像数据
    image_data = image_file.read()
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传头像异常")

    # 将文件名信息保存到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存头像信息失败")

    avatar_url = constants.QINIU_URL_DOMAIN + file_name

    # 返回值
    return jsonify(errno=RET.OK, errmsg="保存头像成功", data={"avatar_url": avatar_url})