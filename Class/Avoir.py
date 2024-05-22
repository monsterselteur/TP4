from connexion import *

class Avoir(Base):
    __tablename__ = 'avoir'
    id_vol = Column(Integer, ForeignKey('vol.id'), primary_key=True, nullable=False)
    id_siege = Column(Integer, ForeignKey('Siege.id'), primary_key=True, nullable=False)
    id_reservation = Column(Integer, ForeignKey('reservation.id'), primary_key=True, nullable=False)
