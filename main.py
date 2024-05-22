from sqlalchemy import Column, Integer, Float, ForeignKey, Text, Date
from connexion import Base, session, engine
from Class import *

Base.metadata.create_all(engine)

