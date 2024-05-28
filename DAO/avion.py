from Database.create import Avion
from connexion import session
from sqlalchemy import update, select, delete

def create_avion(nom, id_comp):
    """
    Créer un avion d'une compagnie.

    Parameters
    ----------
    nom : str
        Le nom de l'avion.
    id_comp : int
        L'identifiant de la compagnie.
    """
    comp = Avion(nom_A=nom,id_compagnie=id_comp)
    session.add(comp)
    session.commit()


def read_avion(id):
    """
    Recherche un avion.

    Parameters
    ----------
    id : int
        L'identifiant de l'avion.

    Returns
    -------
    Avion
        L'objet avion.
    """
    return session.query(Avion).filter(Avion.id == id).first()


def read_all_avion():
    """
    Recherche touts les avions.

    Returns
    -------
    Liste_Avion
        Une liste d'objet avion.
    """
    return session.query(Avion).all()


def update_avion(id, nom, id_comp):
    """
    Met à jour une compagnies.

    Parameters
    ----------
    id : int
        L'identifiant de l'avion.
    nom : str
        Le nom de l'avion.
    id_comp : int
        L'identifiant de la compagnie.
    """
    stmt = (
        update(Avion)
        .where(Avion.id == id)
        .values(nom_Comp=nom,id_comp=id_comp)
    )
    session.execute(stmt)


def delete_avion(id):
    """
    Supprime un Avion.

    Parameters
    ----------
    id : int
        L'identifiant de l'avion.
    """
    stmt = delete(Avion).where(Avion.id == id)
    session.execute(stmt)

