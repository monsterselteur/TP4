from sqlalchemy import Column, Integer, String, Float, ForeignKey, and_, Boolean, Text, Date
from connexion import Base, session, engine
import Utilisateur,Compagnie,Avion,Siege,Pays,Reservation


class Vol(Base):
    __tablename__ = 'vol'
    id = Column(Integer, primary_key=True)
    prix = Column(Float, nullable=False)
    dateDepart = Column(Date, nullable=False)
    dateArrivee = Column(Date, nullable=False)
    id_paysDepart = Column(Integer, ForeignKey('pays.id'), nullable=False)
    id_paysArrivee = Column(Integer, ForeignKey('pays.id'), nullable=False)
    id_avion = Column(Integer, ForeignKey('avion.id'), nullable=False)

class Avoir(Base):
    __tablename__ = 'avoir'
    id_vol = Column(Integer, ForeignKey('vol.id'), primary_key=True, nullable=False)
    id_siege = Column(Integer, ForeignKey('Siege.id'), primary_key=True, nullable=False)
    id_reservation = Column(Integer, ForeignKey('reservation.id'), primary_key=True, nullable=False)

Base.metadata.create_all(engine)

