from Database.create import Vol
from connexion import session
from sqlalchemy import update, select, delete, Date, and_
from DAO import pays


def create_v(prix, dateDepart, dateArrivee, id_paysD, id_paysA, id_avion):
    """
    Créer un vol.

    Parameters
    ----------
    prix : float
        Le prix du vol.
    dateDepart : Date
        La date de départ du vol.
    dateArrivee : Date
        La date d'arrivee du vol.
    id_paysD : int
        L'identifiant du pays de départ du vol.
    id_paysA : int
        L'identifiant du pays d'arrivee du vol.
    id_avion : int
        L'identifiant de l'avion du vol.'
    """
    comp = Vol(
        prix=prix,
        dateDepart=dateDepart,
        dateArrivee=dateArrivee,
        id_paysDepart=id_paysD,
        id_paysArrivee=id_paysA,
        id_avion=id_avion
    )
    session.add(comp)
    session.commit()


def read_v(id):
    """
    Recherche un vol.

    Parameters
    ----------
    id : int
        L'identifiant du vol.

    Returns
    -------
    Vol
        L'objet vol.
    """
    return session.query(Vol).filter(Vol.id == id).first()


def read_name(paysDepart, paysArrivee):
    """
    Recherche tout les vol par les pays de départ et d'arrivée.

    Parameters
    ----------
    paysDepart : str
        Le nom du pays de départ du vol.
    paysArrivee : str
        Le nom du pays d'arrivée du vol.
    Returns
    -------
    lst_Vol
        List d'objet vol.
    """
    return (
        session
        .query(Vol)
        .filter(
            and_(
                Vol.id_paysArrivee == pays.read_name_p(paysArrivee).id,
                Vol.id_paysDepart == pays.read_name_p(paysDepart).id
            )
        ).all()
    )


def read_all_v():
    """
    Recherche touts les vols.

    Returns
    -------
    Liste_Vol
        Une liste d'objet vol.
    """
    return session.query(Vol).all()


def update_v(id, prix, dateDepart, dateArrivee, id_paysD, id_paysA, id_avion):
    """
    Met à jour un vol.

    Parameters
    ----------
    id : int
        L'identifiant du vol.
    prix : float
        Le prix du vol.
    dateDepart : Date
        La date de départ du vol.
    dateArrivee : Date
        La date d'arrivee du vol.
    id_paysD : int
        L'identifiant du pays de départ du vol.
    id_paysA : int
        L'identifiant du pays d'arrivee du vol.
    id_avion : int
        L'identifiant de l'avion du vol.'
    """
    stmt = (
        update(Vol)
        .where(Vol.id == id)
        .values(
            prix=prix,
            dateDepart=dateDepart,
            dateArrivee=dateArrivee,
            id_paysDepart=id_paysD,
            id_paysArrivee=id_paysA,
            id_avion=id_avion
        )
    )
    session.execute(stmt)


def delete_p(id):
    """
    Supprime un vol.

    Parameters
    ----------
    id : int
        L'identifiant du vol.
    """
    stmt = delete(Vol).where(Vol.id == id)
    session.execute(stmt)
