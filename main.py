from sqlalchemy import Column, Integer, String, Float, ForeignKey, and_, Boolean, Text, Date
from connexion import Base, session, engine
from Class import Utilisateur,Compagnie,Avion,Siege,Pays,Reservation


p = Pays.Pays(nom_P="France")
p1 = Pays.Pays(nom_P="Alemagne")
p2 = Pays.Pays(nom_P="Angletaire")
p3 = Pays.Pays(nom_P="Afrique du Sud")
session.add_all([p,p1,p2,p3])
session.commit()
Base.metadata.create_all(engine)

