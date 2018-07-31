# coding:utf-8
from flask import Flask

import redis


# import os
# import sys
# root = os.path.dirname(__file__) + '/..'
# sys.path.append(root)
# from api.model import Base
# target_metadata = Base.metadata
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

@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':

    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=5001)

