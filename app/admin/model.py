# coding:utf-8
from datetime import datetime

from sqlalchemy import ForeignKey, Column, Integer, String, VARCHAR, DateTime, BOOLEAN, FLOAT
from sqlalchemy.orm import relationship

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


class Commodity(db.Model):
    __tablename__ = 'commodity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(60))
    price = Column(FLOAT)
    product_id = Column(VARCHAR(30))
    stock = Column(Integer)

    category= Column(Integer,ForeignKey('commodity_category.id'))
    commodity_category = relationship('Commodity_category',backref=db.backref('commodity', lazy='dynamic'))

    status = Column(Integer)

class Commodity_category(db.Model):
    __tablename__ = 'commodity_category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(60))

class Commodity_recommend(db.Model):
    __tablename__ = 'commodity_recommend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    commodity_id = Column(Integer,ForeignKey('commodity.id'))
    commodity = relationship('Commodity', backref=db.backref('commodity_recommend', lazy='dynamic'))
    desc = Column(VARCHAR(60))

class Commodity_repertory(db.Model):
    __tablename__ = 'commodity_repertory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(45))
    # 进货价格
    purchase_price = Column(FLOAT)
    time = Column(DateTime)
    operator = Column(Integer)
    detail = Column(VARCHAR(80))
    # 供货商
    supplier = Column(VARCHAR(45))
    expiration_date = Column(Integer)
    product_id = Column(VARCHAR(45))

    weight = Column(VARCHAR(20))

    def __init__(self,name,purchase_price,operator,weight):
        self.name = name
        self.purchase_price = purchase_price
        self.operator = operator
        self.weight = weight
        self.supplier = ''


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
    login_status = Column(BOOLEAN)


    def __init__(self,phone_number,passwd,login_status):
        self.nickname = 'abc'
        self.username = 'abc'
        self.phone_number = phone_number
        self.passwd = passwd
        self.login_status = login_status


    # id = Column('id', Integer, primary_key=True)
    # phone_number = Column('phone_number', String(11), index=True)
    # password = Column('password', VARCHAR(40))
    # nickname = Column('nickname', VARCHAR(30), index=True, nullable=True)
    # register_time = Column('register_time',DateTime, default=datetime.now())
    # nickn = Column('nickname1', VARCHAR(30), index=True, nullable=True)
    # head_picture = Column('head_picture', String(100), default='')

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)