


from flask_mail import Message
from app import app
import os
from threading import Thread


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = True

# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') or 'me@example.com'
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') or '123456'

# 发送邮件之间需要在环境变量中加入 用户名和密码
# export MAIL_USERNAME='me@example.com'
# $ export MAIL_PASSWORD='123456'



from flask_mail import Mail
mail = Mail(app)

def sendMail():
    pass

    msg = Message(subject='test subject', sender='CEO James <james.ltesim@gmail.com>',
                  recipients=['james.ltesim@gmail.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b>  body'

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)
