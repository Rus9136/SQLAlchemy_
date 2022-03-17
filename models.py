
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, CheckConstraint, Numeric
from datetime import datetime
from sqlalchemy.orm import declarative_base
metadata = MetaData()
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)



