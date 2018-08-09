# coding:utf-8
from flask import Flask

import redis
from flask_sqlalchemy import SQLAlchemy

from app.config import Conf


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Conf)

    # redis
    app.redis_store = redis.Redis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], decode_responses=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = Conf.MYSQL_INFO
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Mail
    app.config['MAIL_SERVER'] = Conf.MAIL_SERVER
    app.config['MAIL_PORT'] = Conf.MAIL_PORT
    app.config['MAIL_USE_TLS'] = Conf.MAIL_USE_TLS


    # 蓝图
    from app.api.v1_0_0.view import api_v1_0_0 as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0.0')

    from app.api.v1_0_1 import api_v1_0_1 as api_1_1_blueprint
    app.register_blueprint(api_1_1_blueprint, url_prefix='/api/v1.0.1')

    # init
    db.init_app(app)
    return app


app = create_app()




@app.route('/')
def index():

    from app.vender import mail
    mail.sendMail()
    return "Flask is God  Do you know?"

@app.route('/addscheduler')
def addscheduler():
    return "hello world"

# 后台系统

from flask_admin import Admin
admin = Admin(app,name=u'后台管理系统')
from app.admin.views import MyView
admin.add_view(MyView(name=u'Hello'))


if __name__ == '__main__':

    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=5001)