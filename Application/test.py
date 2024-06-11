from tkinter import *
from tkinter import ttk

from DAO import pays, vol, utilisateur
from Database.create import Utilisateur
from Application import InterfacePrincipale

lstPays = pays.read_all_p()

token = {"utilisateur": Utilisateur()}
token["utilisateur"] = None


def nextScreen():
    root.destroy()
    InterfacePrincipale.run()

def login():
    login = entry_login.get()
    mdp = entry_mdp.get()
    user1 = utilisateur.read_mdp_u(login, mdp)
    if user1:
        token["utilisateur"] = user1
        nextScreen()


def register():
    login = entry_login.get()
    mdp = entry_mdp.get()
    token["utilisateur"] = utilisateur.create_u(login, mdp)
    nextScreen()


# creation window
root = Tk()
root.geometry()
root.minsize(460, 271)
root.title('connexion utilisateur')

#ajouter un text
label_title = Label(root, text="Login", font=("Inter", 20))
label_title.pack(side=TOP)

boite = Frame(root)

frame_combo = Frame(boite)

# login
label_login = Label(frame_combo, text="identifiant", font=("Inter", 16))
label_login.pack()
entry_login = Entry(frame_combo)
entry_login.pack()

# mdp
label_mdp = Label(frame_combo, text="mot de passe", font=("Inter", 16))
label_mdp.pack()
entry_mdp = Entry(frame_combo, show="*")
entry_mdp.pack()

frame_combo.pack()

frame_button = Frame(boite)

#button
button_valider = Button(frame_button, text="Log in", font=("Inter", 16), bg="#000000", fg="white", command=login)
button_valider.grid(row=0, column=0, padx=10, pady=10, ipadx=5, ipady=5)

button_registre = Button(frame_button, text="Sign in", font=("Inter", 16), bg="#000000", fg="white", command=register)
button_registre.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5)

button_inconnue = Button(frame_button, text="inconito", font=("Inter", 16), bg="#000000", fg="white", command=nextScreen)
button_inconnue.grid(row=0, column=3, padx=10, pady=10, ipadx=5, ipady=5)

frame_button.pack(pady=10)

boite.pack(pady=10)

root.mainloop()
