from flask import Blueprint, jsonify

from app import db
from app.admin.model import User

api_v1_0_0 = Blueprint('api_v1_0_0',__name__)



import hashlib
from functools import wraps

from flask import request, jsonify, current_app, g

from app import db
from app.admin.model import User

from . import api_v1_0_0

from ..v1_0_0.model import Model_v1_0_0

model = Model_v1_0_0()

def login_check(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # token = request.headers.get('token')
        # if not token:
        #     return jsonify({'code': 0, 'message': '需要验证'})
        #
        # phone_number = current_app.redis_store.get('token:%s' % token)
        # if not phone_number or token != current_app.redis_store.hget('user:%s' % phone_number, 'token'):
        #     return jsonify({'code': 2, 'message': '验证信息错误'})
        model.login_check()
        return f(*args, **kwargs)

    return decorator

@api_v1_0_0.route('/')
def hello_world():
    # api = APITest('http://127.0.0.1:5001')
    # data = api.login('12345678901', '123456')
    # print(data.get('message'))

    return model.hello_world()



# 上次登录接口不安全，要修改一下。一般来说，验证时，都是把用户名，和 密码+随机值+时间戳 的加密方式传过去
# cryption_str就是加密串，是由密码+随机值+时间戳用sha256加密的。传到服务器，服务器也这样加密一下，然后看看2者是不是一致。传输过程不涉及密码传输。就这么简单。
@api_v1_0_0.route('/login', methods=['POST'])
def login():

    phone_number = request.get_json().get('phone_number')
    encryption_str = request.get_json().get('password')
    password = request.get_json().get('password')
    user = User.query.filter_by(phone_number=phone_number).first()

    # if not user:
    #     return jsonify({'code': 0, 'message': '没有此用户'})
    #
    # password_in_sql = user.password
    # if user.password != password:
    #     return jsonify({'code': 0, 'message': '密码错误'})
    #
    # # encryption_str就是加密串，是由密码 + 随机值 + 时间戳用sha256加密的。传到服务器，服务器也这样加密一下，然后看看2者是不是一致。传输过程不涉及密码传输。
    # # s = hashlib.sha256()
    # # s.update(password_in_sql.encode("utf8"))
    # # # s.update(random_str)
    # # # s.update(time_stamp)
    # # server_encryption_str = s.hexdigest()
    # #
    # # print(server_encryption_str,encryption_str)
    # # if server_encryption_str != encryption_str:
    # #     return jsonify({'code': 0, 'message': '密码错误'})


    # # 生成token
    # m = hashlib.md5()
    #
    # m.update(phone_number.encode("utf8"))
    # m.update(password.encode("utf8"))
    # m.update(str(int(time.time())).encode("utf8"))
    # token = m.hexdigest()
    #
    # pipline = current_app.redis_store.pipeline()
    # pipline.hmset('user:%s' % user.phone_number, {'token': token, 'nickname': user.nickname, 'app_online': 1})
    # pipline.set('token:%s' % token, user.phone_number)
    # pipline.expire('token:%s' % token, 3600*24*30)
    # pipline.execute()

    token = model.login(user,password,phone_number)
    return jsonify({'code': 1, 'message': '成功登录', 'nickname': user.nickname, 'token': token})


@api_v1_0_0.route('/user')
@login_check
def user():
   return model.user()


@api_v1_0_0.route('/logout')
@login_check
def logout():
   return model.logout()


@api_v1_0_0.before_request
def before_request():
    # token = request.headers.get('token')
    # phone_number = current_app.redis_store.get('token:%s' % token)
    #
    # print(token,phone_number)
    # if phone_number:
    #     g.current_user = User.query.filter_by(phone_number=phone_number).first()
    #     g.token = token
    return

@api_v1_0_0.teardown_request
def handle_teardown_request(exception):
    db.session.remove()

@api_v1_0_0.route('/add')
def add():
    user = User()
    user.phone_number = 22
    user.password = '22'
    user.nickname = 'bb'


    db.session.add(user)
    db.session.commit()
    return jsonify({'code':1})