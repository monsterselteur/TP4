from sqlalchemy import Integer, Column, Text

from connexion import Base


class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id = Column(Integer, primary_key=True)
    nom_U = Column(Text,nullable=False)
    prenom = Column(Text,nullable=False)