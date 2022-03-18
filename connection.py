import sqlalchemy
from sqlalchemy import MetaData, insert, Table, String, CheckConstraint, SmallInteger, Numeric, Integer, Column, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import relationship
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import insert
from sqlalchemy.orm import Session, sessionmaker

#aclchemyorder

def create_database():
    # Устанвливаем соединение с postgres
    connection = psycopg2.connect(user="postgres", password="123")

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
    #engine = create_engine('postgresql://postgres:123@localhost/aclchemyorder')
    engine = create_engine('postgresql://postgres:123@localhost/'+name_database)
    engine.connect()
    return engine

def core_schemas():

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

def core_add_posts():


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

    conn = connections("aclchemyorder")


    ## добавление записей в табицы по списку
    #conn.execute(insert(items), items_list)
    #conn.execute(insert(orders), order_list)
    #conn.execute(insert(order_lines), order_line_list)

    # s = items.select()
    # r = conn.execute(s)
    #
    # print(r.fetchall())

#####   ORM  #######

def orm_schemas():

    Base = declarative_base()

    engine = create_engine('postgresql://postgres:123@localhost/aclchemyorder')

    class Customer(Base):
        __tablename__ = 'customers'
        id = Column(Integer(), primary_key=True)
        first_name = Column(String(100), nullable=False)
        last_name = Column(String(100), nullable=False)
        username = Column(String(50), nullable=False)
        email = Column(String(200), nullable=False)
        created_on = Column(DateTime(), default=datetime.now)
        updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
        orders = relationship("Order", backref='customer')

    class Item(Base):
        __tablename__ = 'items'
        id = Column(Integer(), primary_key=True)
        name = Column(String(200), nullable=False)
        cost_price = Column(Numeric(10, 2), nullable=False)
        selling_price = Column(Numeric(10, 2), nullable=False)
        quantity = Column(Integer())

    class Order(Base):
        __tablename__ = 'orders'
        id = Column(Integer(), primary_key=True)
        customer_id = Column(Integer(), ForeignKey('customers.id'))
        date_placed = Column(DateTime(), default=datetime.now)
        line_items = relationship("OrderLine", backref='order')

    class OrderLine(Base):
        __tablename__ = 'order_lines'
        id = Column(Integer(), primary_key=True)
        order_id = Column(Integer(), ForeignKey('orders.id'))
        item_id = Column(Integer(), ForeignKey('items.id'))
        quantity = Column(SmallInteger())
        item = relationship("Item")

    Base.metadata.create_all(engine)


engine = create_engine('postgresql://postgres:123@localhost/aclchemyorder')
session = sessionmaker(bind=engine)
sessionLocal = session()

c1 = models.Customer(
    first_name='Rus',
    last_name='daurenov',
    username='RusTD',
    email='3350698@mail.com'
)

sessionLocal.add(c1)
sessionLocal.commit()
