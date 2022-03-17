import sqlalchemy
from sqlalchemy import MetaData, insert, Table, String, CheckConstraint, Numeric, Integer, Column, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#aclchemyorder

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


items_list = [
    {
        "name":"Chair",
        "cost_price": 9.21,
        "selling_price": 10.81,
        "quantity": 6
    },
    {
        "name":"Pen",
        "cost_price": 3.45,
        "selling_price": 4.51,
        "quantity": 3
    },
    {
        "name":"Headphone",
        "cost_price": 15.52,
        "selling_price": 16.81,
        "quantity": 50
    },
    {
        "name":"Travel Bag",
        "cost_price": 20.1,
        "selling_price": 24.21,
        "quantity": 50
    },
    {
        "name":"Keyboard",
        "cost_price": 20.12,
        "selling_price": 22.11,
        "quantity": 50
    },
    {
        "name":"Monitor",
        "cost_price": 200.14,
        "selling_price": 212.89,
        "quantity": 50
    },
    {
        "name":"Watch",
        "cost_price": 100.58,
        "selling_price": 104.41,
        "quantity": 50
    },
    {
        "name":"Water Bottle",
        "cost_price": 20.89,
        "selling_price": 25.00,
        "quantity": 50
    },
]

order_list = [
    {
        "customer_id": 1
    },
    {
        "customer_id": 1
    }
]

order_line_list = [
    {
        "order_id": 1,
        "item_id": 1,
        "quantity": 5
    },
    {
        "order_id": 1,
        "item_id": 2,
        "quantity": 2
    },
    {
        "order_id": 1,
        "item_id": 3,
        "quantity": 1
    },
    {
        "order_id": 2,
        "item_id": 1,
        "quantity": 5
    },
    {
        "order_id": 2,
        "item_id": 2,
        "quantity": 5
    },
]



conn = connections("aclchemyorder")
# conn.execute(insert(items), items_list)
# conn.execute(insert(orders), order_list)
# conn.execute(insert(order_lines), order_line_list)
#

s = customers.select()
r = conn.execute(s)

print(r.fetchall())