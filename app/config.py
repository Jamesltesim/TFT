


class Config(object):
    SECRET_KEY = 'saduhsuaihfe332r32rfo43rtn3noiYUG9jijoNF23'
    QINIU_ACCESS_KEY = 'hP7WNic×××××××××××××××××××××××××oZfrVs6'
    QINIU_SECRET_KEY = 'bBZ×××××××××××××××××××××××××××××××××VAV'
    BUCKET_NAME = 'dameinv'


class DevelopmentConfig(Config):
    DEBUG = True

    # Redis
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 4
    REDIS_PASSWORD = '123456'

    # Mysql
    MYSQL_INFO = "mysql+pymysql://root:12345678@localhost:3306/test01?charset=utf8"


    # Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT   = 587
    # app.config['MAIL_USE_SSL'] = True
    MAIL_USE_TLS = True


class ProductionConfig(Config):
    DEBUG = False

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 4
    REDIS_PASSWORD = '123456'

    MYSQL_INFO = "mysql+pymysql://root:12345678@192.168.56.102:3306/test01?charset=utf8"

    # Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    # app.config['MAIL_USE_SSL'] = True
    MAIL_USE_TLS = True

Conf = DevelopmentConfig