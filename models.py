
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime


engine = create_engine("postgresql+psycopg2://postgres:1@localhost/sqlalchemy_tuts")

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
customers = metadata_obj.tables['customers']

ins = customers.insert().values(
    first_name = 'Rus',
    last_name = 'Daurenov',
    username = 'RusTD',
    email = 'moseend@mail.com',

)

conn = engine.connect()
r = conn.execute(ins)
