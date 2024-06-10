from Database.create import Utilisateur
from connexion import session
from sqlalchemy import update, select, delete


def create_u(login, mdp):
    """
    Créer un utilisateur.

    Parameters
    ----------
    login : str
        Le login de l'utilisateur.
    mdp : str
        Le mot de passe de l'utilisateur.
    """
    user = Utilisateur(login=login, mdp=mdp)
    session.add(user)
    session.commit()
    return user


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


def read_mdp_u(login, mdp):
    """
    Recherche un utilisateur.

    Parameters
    ----------
    login : str
        Le login de l'utilisateur.
    mdp : str
        Le mot de passe de l'utilisateur.
    Returns
    -------
    Utilisateur
        Une objet utilisateur.
    """
    return session.query(Utilisateur).filter(
        Utilisateur.login == login,
        Utilisateur.mdp == mdp
    ).first()

def read_all_u():
    """
    Recherche touts les utilisateurs.

    Returns
    -------
    Liste_Utilisateur
        Une liste d'objet utilisateur.
    """
    return session.query(Utilisateur).all()


def update_u(id, login, mdp):
    """
    Met à jour un utilisateur.

    Parameters
    ----------
    id : int
        L'identifiant de l'utilisateur.
    login : str
        Le login de l'utilisateur.
    mdp : str
        Le mot de passe de l'utilisateur.
    """
    stmt = (
        update(Utilisateur)
        .where(Utilisateur.id == id)
        .values(login=login, mdp=mdp)
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
