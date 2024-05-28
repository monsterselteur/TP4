from Database.create import Utilisateur
from connexion import session
from sqlalchemy import update, select, delete


def create_u(nom, prenom):
    """
    Créer un utilisateur.

    Parameters
    ----------
    nom : str
        Le nom de l'utilisateur.
    prenom : str
        Le prenom de l'utilisateur.
    """
    user = Utilisateur(nom_U=nom, prenom=prenom)
    session.add(user)
    session.commit()


def read_u(id):
    """
    Recherche un utilisateur.

    Parameters
    ----------
    id : int
        L'identifiant de l'utilisateur.

    Returns
    -------
    Utilisateur
        Une objet utilisateur.
    """
    return session.query(Utilisateur).filter(Utilisateur.id == id).first()


def read_all_u():
    """
    Recherche touts les utilisateurs.

    Returns
    -------
    Liste_Utilisateur
        Une liste d'objet utilisateur.
    """
    return session.query(Utilisateur).all()


def update_u(id, nom, prenom):
    """
    Met à jour un utilisateur.

    Parameters
    ----------
    id : int
        L'identifiant de l'utilisateur.
    nom : str
        Le nom de l'utilisateur.
    prenom : str
        Le prenom de l'utilisateur.
    """
    stmt = (
        update(Utilisateur)
        .where(Utilisateur.id == id)
        .values(nom_U=nom, prenom=prenom)
    )
    session.execute(stmt)


def delete_u(id):
    """
    Supprime un utilisateur.

    Parameters
    ----------
    id : int
        L'identifiant de l'utilisateur.
    """
    stmt = delete(Utilisateur).where(Utilisateur.id == id)
    session.execute(stmt)
