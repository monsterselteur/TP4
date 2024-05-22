from sqlalchemy import Integer, Column, Text

from connexion import Base


class Compagnie(Base):
    __tablename__ = 'compagnie'
    id = Column(Integer, primary_key=True)
    nom_Comp = Column(Text,nullable=False)