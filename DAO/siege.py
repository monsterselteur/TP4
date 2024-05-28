from Database.create import Siege
from connexion import session
from sqlalchemy import update, select, delete

def create_s(nom, id_avion):
    """
    Créer un siege d'un avion.

    Parameters
    ----------
    nom : str
        Le nom du siege.
    id_avion : int
        L'identifiant de l'avion.
    """
    comp = Siege(nom_S=nom,id_avion=id_avion)
    session.add(comp)
    session.commit()


def read_s(id):
    """
    Recherche un siege.

    Parameters
    ----------
    id : int
        L'identifiant du siege.

    Returns
    -------
    Siege
        L'objet siege.
    """
    return session.query(Siege).filter(Siege.id == id).first()


def read_all_siege():
    """
    Recherche touts les sieges.

    Returns
    -------
    Liste_Siege
        Une liste d'objet siege.
    """
    return session.query(Siege).all()


def update_avion(id, nom, id_avion):
    """
    Met à jour un siege.

    Parameters
    ----------
    id : int
        L'identifiant du siege.
    nom : str
        Le nom de du siege.
    id_avion : int
        L'identifiant de l'avion.
    """
    stmt = (
        update(Siege)
        .where(Siege.id == id)
        .values(nom_Comp=nom,id_avion=id_avion)
    )
    session.execute(stmt)


def delete_c(id):
    """
    Supprime un siege.

    Parameters
    ----------
    id : int
        L'identifiant du siege.
    """
    stmt = delete(Siege).where(Siege.id == id)
    session.execute(stmt)

