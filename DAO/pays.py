from Database.create import Pays
from connexion import session
from sqlalchemy import update, select, delete

def create_p(nom):
    """
    Créer un pays.

    Parameters
    ----------
    nom : str
        Le nom du pays.
    """
    comp = Pays(nom_P=nom)
    session.add(comp)
    session.commit()


def read_p(id):
    """
    Recherche un pays.

    Parameters
    ----------
    id : int
        L'identifiant du pays.

    Returns
    -------
    Pays
        L'objet pays.
    """
    return session.query(Pays).filter(Pays.id == id).first()


def read_all_p():
    """
    Recherche touts les pays.

    Returns
    -------
    Liste_Pays
        Une liste d'objet pays.
    """
    return session.query(Pays).all()


def update_p(id, nom):
    """
    Met à jour un pays.

    Parameters
    ----------
    id : int
        L'identifiant du pays.
    nom : str
        Le nom du pays.
    """
    stmt = (
        update(Pays)
        .where(Pays.id == id)
        .values(nom_P=nom)
    )
    session.execute(stmt)


def delete_p(id):
    """
    Supprime un pays.

    Parameters
    ----------
    id : int
        L'identifiant du pays.
    """
    stmt = delete(Pays).where(Pays.id == id)
    session.execute(stmt)

