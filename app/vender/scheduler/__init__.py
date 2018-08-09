# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app/vender/scheduler/log/log.txt',
                    filemode='a')




def aps_test():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好')




scheduler = BlockingScheduler()
# 5秒整倍数，就执行这个函数
scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
scheduler.start()

# scheduler.add_job(aps_test, 'interval', seconds=5)
# scheduler.start()