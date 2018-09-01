import hashlib

from flask import request, jsonify, current_app, g
import time


class Model_v1_0_0:
    def __init__(self):
        print('I\'m model_v1_0_0')

    def hello_world(self):
        return 'v1.0.0'

    def login_check(self):
        token = request.headers.get('token')
        if not token:
            return jsonify({'code': 0, 'message': '需要验证'})

        phone_number = current_app.redis_store.get('token:%s' % token)
        if not phone_number or token != current_app.redis_store.hget('user:%s' % phone_number, 'token'):
            return jsonify({'code': 2, 'message': '验证信息错误'})


    def login(self,user,password,phone_number):
        if not user:
            return jsonify({'code': 0, 'message': '没有此用户'})

        password_in_sql = user.password
        if user.password != password:
            return jsonify({'code': 0, 'message': '密码错误'})

        # encryption_str就是加密串，是由密码 + 随机值 + 时间戳用sha256加密的。传到服务器，服务器也这样加密一下，然后看看2者是不是一致。传输过程不涉及密码传输。
        # s = hashlib.sha256()
        # s.update(password_in_sql.encode("utf8"))
        # # s.update(random_str)
        # # s.update(time_stamp)
        # server_encryption_str = s.hexdigest()
        #
        # print(server_encryption_str,encryption_str)
        # if server_encryption_str != encryption_str:
        #     return jsonify({'code': 0, 'message': '密码错误'})

        # 生成token
        m = hashlib.md5()

        m.update(phone_number.encode("utf8"))
        m.update(password.encode("utf8"))
        m.update(str(int(time.time())).encode("utf8"))
        token = m.hexdigest()

        pipline = current_app.redis_store.pipeline()
        pipline.hmset('user:%s' % user.phone_number, {'token': token, 'nickname': user.nickname, 'app_online': 1})
        pipline.set('token:%s' % token, user.phone_number)
        pipline.expire('token:%s' % token, 3600 * 24 * 30)
        pipline.execute()

        return token

    def user(self):
        print('user接口 入口')
        user = g.current_user
        nickname = current_app.redis_store.hget('user:%s' % user.phone_number, 'nickname')
        print('user接口 返回 数据')
        return jsonify({'code': 1, 'nickname': nickname, 'phone_number': user.phone_number})

    def logout(self):
        user = g.current_user
        pipline = current_app.redis_store.pipeline()
        pipline.delete('token:%s' % g.token)
        pipline.hmset('user:%s' % user.phone_number, {'app_online': 0})
        pipline.execute()

        return jsonify({'code': 1, 'message': '成功注销'})
