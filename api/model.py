# coding:utf-8
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Text, DateTime,\
    and_, or_, SmallInteger, Float, DECIMAL, desc, asc, Table, join, event
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session, aliased, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm.collections import attribute_mapped_collection
import datetime

from config import Conf

engine = create_engine(Conf.MYSQL_INFO, pool_recycle=7200)

Base = declarative_base()

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    phone_number = Column('phone_number', String(11), index=True)
    password = Column('password', String(30))
    nickname = Column('nickname', String(30), index=True, nullable=True)
    register_time = Column('register_time', DateTime, index=True, default=datetime.datetime.now)

    # head_picture = Column('head_picture', String(100), default='')

if __name__ == '__main__':
    Base.metadata.create_all(engine)