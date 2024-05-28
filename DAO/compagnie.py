from Database.create import Compagnie
from connexion import session
from sqlalchemy import update, select, delete

def create_c(nom):
    """
    Créer une compagnie.

    Parameters
    ----------
    nom : str
        Le nom de la compagnie.
    """
    comp = Compagnie(nom_Comp=nom)
    session.add(comp)
    session.commit()


def read_c(id):
    """
    Recherche une compagnie.

    Parameters
    ----------
    id : int
        L'identifiant de la compagnie.

    Returns
    -------
    Compagnie
        L'objet compagnie.
    """
    return session.query(Compagnie).filter(Compagnie.id == id).first()


def read_all_c():
    """
    Recherche toutes les compagnies.

    Returns
    -------
    Liste_Compagnie
        Une liste d'objet compagnie.
    """
    return session.query(Compagnie).all()


def update_c(id, nom):
    """
    Met à jour une compagnies.

    Parameters
    ----------
    id : int
        L'identifiant de la compagnie.
    nom : str
        Le nouveau nom de la compagnie.
    """
    stmt = (
        update(Compagnie)
        .where(Compagnie.id == id)
        .values(nom_Comp=nom)
    )
    session.execute(stmt)


def delete_c(id):
    """
    Supprime une compagnies.

    Parameters
    ----------
    id : int
        L'identifiant de la compagnie.
    """
    stmt = delete(Compagnie).where(Compagnie.id == id)
    session.execute(stmt)

