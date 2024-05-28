from Database.create import Reservation
from connexion import session
from sqlalchemy import update, select, delete

def create_r(id_u):
    """
    Créer une reservation.

    Parameters
    ----------
    id_u : int
        Le nom de l'utilisateur de la reservation.
    """
    comp = Reservation(id_utilisateur=id_u)
    session.add(comp)
    session.commit()


def read_r(id):
    """
    Recherche une reservation.

    Parameters
    ----------
    id : int
        L'identifiant de la reservation.

    Returns
    -------
    Pays
        L'objet pays.
    """
    return session.query(Reservation).filter(Reservation.id == id).first()


def read_all_r():
    """
    Recherche toutes les reservations.

    Returns
    -------
    Liste_Reservations
        Une liste d'objet reservations.
    """
    return session.query(Reservation).all()


def update_r(id, id_u):
    """
    Met à jour une reservation.

    Parameters
    ----------
    id : int
        L'identifiant de la reservation.
    id_u : int
        L'identifiant de l'utilisateur de la reservation.
    """
    stmt = (
        update(Reservation)
        .where(Reservation.id == id)
        .values(id_utilisateur=id_u)
    )
    session.execute(stmt)


def delete_r(id):
    """
    Supprime une reservation.

    Parameters
    ----------
    id : int
        L'identifiant de la reservation.
    """
    stmt = delete(Reservation).where(Reservation.id == id)
    session.execute(stmt)

