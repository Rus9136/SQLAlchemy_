import sqlalchemy
from sqlalchemy import MetaData, Table, String, CheckConstraint, Numeric, Integer, Column, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database():
    # Устанвливаем соединение с postgres
    connection = psycopg2.connect(user="postgres", password="1")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    # Создаем базу данных
    sql_create_database = cursor.execute('CREATE DATABASE aclchemyorder')

    cursor.close()
    connection.close()

def connections(name_database):

    # Соединение с Sqlite3
    # engine = sqlalchemy.create_engine('sqlite:///test.db')

    engine = create_engine('postgresql://postgres:1@localhost/'+name_database)
    engine.connect()
    return engine

def schemas_core():

    metadata = MetaData()

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

    items = Table('items', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('name', String(200), nullable=False),
                  Column('cost_price', Numeric(10, 2), nullable=False),
                  Column('selling_price', Numeric(10, 2), nullable=False),
                  Column('quantity', Integer(), nullable=False),
                  CheckConstraint('quantity > 0', name='quantity_check')
                  )

    orders = Table('orders', metadata,
                   Column('id', Integer(), primary_key=True),
                   Column('customer_id', ForeignKey('customers.id')),
                   Column('date_placed', DateTime(), default=datetime.now),
                   Column('date_shipped', DateTime())
                   )

    order_lines = Table('order_lines', metadata,
                        Column('id', Integer(), primary_key=True),
                        Column('order_id', ForeignKey('orders.id')),
                        Column('item_id', ForeignKey('items.id')),
                        Column('quantity', Integer())
                        )
    # for i in metadata.tables:
    #     print(metadata.tables[i])

    engine = connections("aclchemyorder")

    metadata.create_all(engine)
