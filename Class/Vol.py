from mysql.connector import Date

from connexion import *

base = Base()
ses = session()

class Vol(Base):
    __tablename__ = 'vol'
    id = Column(Integer, primary_key=True)
    prix = Column(Float, nullable=False)
    dateDepart = Column(Date, nullable=False)
    dateArrivee = Column(Date, nullable=False)
    id_paysDepart = Column(Integer, ForeignKey('pays.id'), nullable=False)
    id_paysArrivee = Column(Integer, ForeignKey('pays.id'), nullable=False)
    id_avion = Column(Integer, ForeignKey('avion.id'), nullable=False)


