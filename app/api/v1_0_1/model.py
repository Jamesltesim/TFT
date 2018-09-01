from app.api.v1_0_0.model import Model_v1_0_0


class Model_v1_0_1(Model_v1_0_0):
    def __init__(self):
        print('I\'m App_v1_0_1')
    def hello_world(self):
        return '1.0.1'