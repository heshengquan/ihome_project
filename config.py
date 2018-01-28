# -*- coding:utf-8 -*-
import redis


class Config(object):
    """工程的配置信息"""
    SECRET_KEY = "asdkjheu86iw88q88ra446sf"

    # mysql数据库连接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python02"
    # 跟踪数据库变化
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # REDIS数据库连接地址
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session用到的配置信息
    SESSION_TYPE = "redis"  # 让session存储到redis中
    SESSION_USE_SIGNER = True  # 让cookie中的session_id做加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用的redis实例

    PERMANENT_SESSION_LIFETIME = 86400  # session的有效期，单位秒

class DevelopmentConfig(Config):
    """开发模式使用的配置信息"""
    DEBUG=True
    # 支付宝
    ALIPAY_APPID = "2016081600258081"
    ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"

class ProductionConfig(Config):
    """生产模式 线上模式的配置信息"""
    pass

config_dict={
    "develope":DevelopmentConfig,
    "product":ProductionConfig
}
