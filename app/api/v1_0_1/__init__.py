from flask import Blueprint
api_v1_0_1 = Blueprint('api_v1_0_1',__name__)

from ..v1_0_1.model import Model_v1_0_1


app = Model_v1_0_1()


@api_v1_0_1.route('/')
def hello_world():

    return app.hello_world()