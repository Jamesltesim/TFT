
2018/8/1



gunicorn 守护进程开启
gunicorn -D -b localhost:5001 app:app

杀死gunicorn进程
ps -e |grep gunicorn|awk '{print $1}'|xargs kill -9




1
生成requirements.txt文件

pip freeze > requirements.txt

安装requirements.txt依赖

pip install -r requirements.txt



2.virtualenv

    1）安装virtualenv

    pip install --upgrade pip
    pip install virtualenv

    2）创建一个使用python3的虚拟环境：

    virtualenv -p /usr/bin/python3 py35env

    3）激活py35env虚拟环境：
    source py35env/bin/active




3.mysql
根据脚本生成表
mysql> source /home/james/python/TFT/mysql.sql





4 sqlalchemy 常用查询方法
#按用户名摸糊查询
trans_details.query.join(Uses).filter(Users.username.like('%xx%'))
#select xxx from trans_details inner join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

#左外联接(left join)
trans_details.query.outerjoin(Uses).filter(Users.username.like('%xx%'))
#select xxx from trans_details left outer join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

#以上是已经设置好外键,它自动找到关联的字段.也可以自己指定:
trans_details.query.join(Uses,trans_details.user_id==Users.id).filter(Users.username.like('%xx%'))
#select xxx from trans_details inner join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

#另外一个更复杂的例子:
q=db.session.query(Credit_bills_details.no,Credit_bills_details.amount,Cards.no).outerjoin(Card_trans_details,
Credit_bills_details.no==Card_trans_details.trans_no).join(Cards,Card_trans_details.to_card_id==Cards.id)\
.filter(Credit_bills_details.credit_bill_id==3)


#SELECT credit_bills_details.no AS credit_bills_details_no, credit_bills_details.amount AS credit_bills_details_amount, cards.no AS cards_no
# FROM credit_bills_details LEFT OUTER JOIN card_trans_details ON credit_bills_details.no = card_trans_details.trans_no INNER JOIN cards
# ON card_trans_details.to_card_id = cards.id  WHERE credit_bills_details.credit_bill_id = %s



5. flask-migrate
(venv) $ python manage.py db init
(venv) $ python manage.py db migrate
(venv) $ python hello.py db upgrade
*第一次迁移实际上相当于调用db.create_all()，但在后续迁移中，upgrade命令对表实施更新操作但不影响表中的内容。