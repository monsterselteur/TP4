from sqlalchemy import Integer, Column, Text, ForeignKey

from connexion import Base


class Siege(Base):
    __tablename__ = 'Siege'
    id = Column(Integer, primary_key=True)
    nom_S = Column(Text,nullable=False)
    id_avion = Column(Integer, ForeignKey('avion.id'),nullable=False)