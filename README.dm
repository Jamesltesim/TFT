
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









##################################################################################
#服务器压力测试工具
##################################################################################

一、http_load
程序非常小，解压后也不到100K
http_load以并行复用的方式运行，用以测试web服务器的吞吐量与负载。
但是它不同于大多数压力测试工具，它可以以一个单一的进程运行，一般不会把客户机搞死。
还可以测试HTTPS类的网站请求。
下载地址：http://acme.com/software/http_load/http_load-12mar2006.tar.gz

安装很简单

#tar zxvf http_load-12mar2006.tar.gz
#cd http_load-12mar2006
#make && make install
基本用法：

http_load  -p 并发访问进程数  -s 访问时间  需要访问的URL文件
参数其实可以自由组合，参数之间的选择并没有什么限制。
比如你写成http_load  -parallel  5  -seconds  300  urllist.txt也是可以的。
我们把参数给大家简单说明一下。
-parallel   简写-p ：含义是并发的用户进程数。
-fetches   简写-f ：含义是总计的访问次数
-rate        简写-p ：含义是每秒的访问频率
-seconds 简写-s ：含义是总计的访问时间

准备URL文件：urllist.txt，文件格式是每行一个URL，URL最好超过50－100个测试效果比较好。

文件格式如下：

http://www.qixing318.com/
http://www.qixing318.com/blog/
http://www.qixing318.com/signin/
http://www.qixing318.com/signup/

例如：

http_load -p 30 -s 60  urllist.txt
参数了解了，我们来看运行一条命令来看看它的返回结果如下：



结果分析：

1、294 fetches, 30 max parallel, 3.83835e+06 bytes, in 60.0026 seconds
说明在上面的测试中运行了294个请求，最大的并发进程数是30，总计传输的数据是3.83835e+06bytes，运行的时间是60.0026秒
2、13055.6 mean bytes/connection
说明每一连接平均传输的数据量3.83835e+06/294=13055.6
3、4.89979 fetches/sec, 63969.7 bytes/sec
说明每秒的响应请求为4.89979，每秒传递的数据为63969.7 bytes/sec
4、msecs/connect: 312.009 mean, 1319.57 max, 209.994 min
说明每连接的平均响应时间是312.009 msecs，最大的响应时间1319.57 msecs，最小的响应时间209.994 msecs
5、msecs/first-response: 1191.01 mean, 10212.4 max, 220.78 min
6、HTTP response codes:
    code 200  --  127
    code 502  --  166
说明打开响应页面的类型
如果403的类型过多，那可能要注意是否系统遇到了瓶颈。
特殊说明：
测试结果中主要的指标是 fetches/sec、msecs/connect 这个选项，即服务器每秒能够响应的查询次数。
用这个指标来衡量性能。似乎比 apache的ab准确率要高一些，也更有说服力一些。
Qpt-每秒响应用户数和response time，每连接响应用户时间。
测试的结果主要也是看这两个值。
当然仅有这两个指标并不能完成对性能的分析，我们还需要对服务器的cpu、men进行分析，才能得出结论。




##################################################################################
#服务器压力测试工具
##################################################################################

