# coding:utf-8
from datetime import datetime

from sqlalchemy import  ForeignKey, Column, Integer, String, VARCHAR, DateTime





from .. import db

# engine = create_engine(Conf.MYSQL_INFO, pool_recycle=7200)
#
#
# Base = declarative_base()
#
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base.query = db_session.query_property()



class User(db.Model):
    __tablename__ = 'user'

    # id = Column( Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    nickname = Column(VARCHAR(45))
    phone_number = Column(VARCHAR(45))
    username = Column(VARCHAR(80))
    passwd = Column(VARCHAR(80))
    register_time = Column(DateTime)
    header_icon_url = Column(VARCHAR(60))
    sex = Column(Integer)


    def __init__(self,phone_number,passwd):
        self.nickname = 'abc'
        self.username = 'abc'
        self.phone_number = phone_number
        self.passwd = passwd

    # id = Column('id', Integer, primary_key=True)
    # phone_number = Column('phone_number', String(11), index=True)
    # password = Column('password', VARCHAR(40))
    # nickname = Column('nickname', VARCHAR(30), index=True, nullable=True)
    # register_time = Column('register_time',DateTime, default=datetime.now())
    # nickn = Column('nickname1', VARCHAR(30), index=True, nullable=True)
    # head_picture = Column('head_picture', String(100), default='')

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)