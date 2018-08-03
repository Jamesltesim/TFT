
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
