
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, CheckConstraint, Numeric
from datetime import datetime

metadata = MetaData()

class Customers():


    customers = Table('customers', metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('first_name', String(100), nullable=False),
                      Column('last_name', String(100), nullable=False),
                      Column('username', String(50), nullable=False),
                      Column('email', String(200), nullable=False),
                      Column('address', String(200), nullable=False),
                      Column('town', String(50), nullable=False),
                      Column('created_on', DateTime(), default=datetime.now),
                      Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                      )


class Item():
    items = Table('items', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('name', String(200), nullable=False),
                  Column('cost_price', Numeric(10, 2), nullable=False),
                  Column('selling_price', Numeric(10, 2), nullable=False),
                  Column('quantity', Integer(), nullable=False),
                  CheckConstraint('quantity > 0', name='quantity_check')
                  )

