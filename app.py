# coding:utf-8
from flask import Flask

import redis


# import os
# import sys
# root = os.path.dirname(__file__) + '/..'
# sys.path.append(root)
# from api.model import Base
# target_metadata = Base.metadata
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from config import Conf

def create_app():
    app = Flask(__name__)
    app.config.from_object(Conf)
    app.redis_store = redis.Redis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], decode_responses=True)

    from api.v1_0_0.view import api_v1_0_0 as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0.0')

    from api.v1_0_1.view import api_v1_0_1 as api_1_1_blueprint
    app.register_blueprint(api_1_1_blueprint, url_prefix='/api/v1.0.1')

    return app


app = create_app()
# engine = create_engine(Conf.MYSQL_INFO, pool_recycle=7200)
# db = SQLAlchemy(app)

@app.route('/')
def index():

    return "Flask is God  Do you know?"

@app.route('/addscheduler')
def addscheduler():
    from vender import scheduler
    return "hello world"

# 后台系统

from flask_admin import Admin
admin = Admin(app,name=u'后台管理系统')
from admin.views import MyView
admin.add_view(MyView(name=u'Hello'))


if __name__ == '__main__':

    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=5001)

