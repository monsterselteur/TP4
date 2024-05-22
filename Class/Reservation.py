from sqlalchemy import Integer, Column, ForeignKey

from connexion import Base


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, nullable=False)
    id_utilisateur = Column(Integer, ForeignKey('utilisateur.id'), primary_key=True, nullable=False)
