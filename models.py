
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, insert, Table, String, CheckConstraint, SmallInteger, Numeric, Integer, Column, Text, DateTime, Boolean, ForeignKey,Date
from datetime import datetime, date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

from database import Base

metadata = MetaData()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(Date)
    category = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)
    user = relationship('User', backref='operations')


