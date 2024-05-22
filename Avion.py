from sqlalchemy import Column, Integer, Text, ForeignKey

from connexion import Base


class Avion(Base):
    __tablename__ = 'avion'
    id = Column(Integer, primary_key=True)
    nom_A = Column(Text,nullable=False)
    id_compagnie = Column(Integer, ForeignKey('compagnie.id'),nullable=False)