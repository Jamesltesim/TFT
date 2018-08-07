

from . import api_v1_0_1

from app.api.v1_0_0.view import App_v1_0_0


class App_v1_0_1(App_v1_0_0):
    def __init__(self):
        print('I\'m App_v1_0_1')


app = App_v1_0_1()


@api_v1_0_1.route('/')
def hello_world():

    return app.hello_world()