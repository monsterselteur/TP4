from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey,DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+mysqlconnector://root:Ddpassword@localhost:3308/aviation")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()