


class Config(object):
    SECRET_KEY = 'saduhsuaihfe332r32rfo43rtn3noiYUG9jijoNF23'
    QINIU_ACCESS_KEY = 'hP7WNic×××××××××××××××××××××××××oZfrVs6'
    QINIU_SECRET_KEY = 'bBZ×××××××××××××××××××××××××××××××××VAV'
    BUCKET_NAME = 'dameinv'


class DevelopmentConfig(Config):
    DEBUG = True

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 4
    REDIS_PASSWORD = '123456'

    MYSQL_INFO = "mysql+pymysql://root:123456@192.168.56.104:3306/test01?charset=utf8"


class ProductionConfig(Config):
    DEBUG = False

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 4
    REDIS_PASSWORD = '123456'

    MYSQL_INFO = "mysql+pymysql://root:123456@192.168.56.102:3306/test01?charset=utf8"

Conf = DevelopmentConfig