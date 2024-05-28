from Database.create import Utilisateur
from connexion import session
from sqlalchemy import update, select, delete


def create_u(nom, prenom):
    """Créer une utilisateur avec le nom et le prénom passés en paramètre."""
    user = Utilisateur(nom_U=nom, prenom=prenom)
    session.add(user)
    session.commit()


def read_u(id):
    """Retourne l'utilisateur trouver grace a l'id."""
    return session.query(Utilisateur).filter(Utilisateur.id == id).first()


def read_all_u():
    """Retourne une liste de tout les utilisateurs."""
    return session.query(Utilisateur)


def update_u(id, nom, prenom):
    """Modifier l'utilisateur avec l'id"""
    stmt = (
        update(Utilisateur)
        .where(Utilisateur.id == id)
        .values(nom_U=nom, prenom=prenom)
    )
    session.execute(stmt)


def delete_u(id):
    """Supprime l'utilisateur avec l'id."""
    stmt = delete(Utilisateur).where(Utilisateur.id == id)
    session.execute(stmt)
