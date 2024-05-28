from sqlalchemy import Column, Integer, Float, ForeignKey, Text, Date
from connexion import Base, engine

class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id = Column(Integer, primary_key=True)
    nom_U = Column(Text,nullable=False)
    prenom = Column(Text,nullable=False)
class Compagnie(Base):
    __tablename__ = 'compagnie'
    id = Column(Integer, primary_key=True)
    nom_Comp = Column(Text,nullable=False)
class Avion(Base):
    __tablename__ = 'avion'
    id = Column(Integer, primary_key=True)
    nom_A = Column(Text,nullable=False)
    id_compagnie = Column(Integer, ForeignKey('compagnie.id'),nullable=False)
class Siege(Base):
    __tablename__ = 'Siege'
    id = Column(Integer, primary_key=True)
    nom_S = Column(Text,nullable=False)
    id_avion = Column(Integer, ForeignKey('avion.id'),nullable=False)
class Pays(Base):
    __tablename__ = 'pays'
    id = Column(Integer, primary_key=True)
    nom_P = Column(Text,nullable=False)
class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, nullable=False)
    id_utilisateur = Column(Integer, ForeignKey('utilisateur.id'), primary_key=True, nullable=False)
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