from sqlalchemy import Integer, Column, Text

from connexion import Base


class Pays(Base):
    __tablename__ = 'pays'
    id = Column(Integer, primary_key=True)
    nom_P = Column(Text,nullable=False)