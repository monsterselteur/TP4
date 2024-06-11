from calendar import calendar
import random
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry

from DAO import pays
from DAO import reservation
from DAO import utilisateur
from DAO import vol
from DAO import siege
from DAO import avion
from DAO import compagnie

from Database import create

import tkinter.messagebox

import sys

import calendar
from sqlalchemy import false, true


def run():
    root = Tk()
    root.geometry('600x400')
    root.title('Gestion de Compagnie Aérienne')

    frame = LabelFrame(root, text="      BIENVENUE SUR LA PAGE DE RESERVATION DES VOLS", bg='white', font=("", 16),
                       borderwidth=0, relief='sunken')
    frame.pack(pady=50, fill=BOTH)

    frame1 = LabelFrame(frame, bg='white', font=("", 16), borderwidth=0, relief='sunken')
    frame1.pack(pady=40, fill=BOTH, expand=True)

    label = Label(frame1, text="       Pays de départ : ", font=("", 16), borderwidth=5, padx=10, relief='sunken')
    label.grid(row=0, column=0)

    label1 = Label(frame1, text="Pays de destination : ", font=("", 16), borderwidth=5, padx=10, relief='sunken')
    label1.grid(row=1, column=0)

    combobox = ttk.Combobox(frame1, values=(pays.read_all_p()), font=("", 16))
    combobox.grid(row=0, column=1)

    combobox1 = ttk.Combobox(frame1, values=(pays.read_all_p()), font=("", 16))
    combobox1.grid(row=1, column=1)

    cal = DateEntry(frame1, font=("", 16), selectionmode='date', borderwidth=20, padx=10, relief='sunken')
    cal.grid(row=2, column=1)
    cal2 = DateEntry(frame1, font=("", 16), selectionmode='date', borderwidth=20, padx=10, relief='sunken')
    cal2.grid(row=3, column=1)

    label2 = Label(frame1, text="    Date de depart     : ", font=("", 16), borderwidth=5, padx=10, relief='sunken')
    label2.grid(row=2, column=0)

    label3 = Label(frame1, text="    Date d'arrive      : ", font=("", 16), borderwidth=5, padx=10, relief='sunken')
    label3.grid(row=3, column=0)

    def InfoUser():
        rootUser = Tk()
        rootUser.geometry('610x450')
        rootUser.title("User information")

        nameframe = LabelFrame(rootUser, text='              User Information \n\n', font=("", 16), borderwidth=0,
                               relief='sunken')
        nameframe.pack(pady=20, fill=BOTH)

        labelName = Label(nameframe, text="              \n\nNom : ", font=("", 16), borderwidth=0, relief='sunken')
        labelName.grid(row=0, column=0)

        labelSurname = Label(nameframe, text="      \n\nSurname : \n\n", font=("", 16), borderwidth=0, relief='sunken')
        labelSurname.grid(row=1, column=0)

        global entrySurname
        entrySurname = Entry(nameframe, font=("", 16))
        global entryName
        entryName = Entry(nameframe, font=("", 16))

        entrySurname.grid(row=1, column=1)
        entryName.grid(row=0, column=1)

        nbplace = Label(nameframe, text="Nombre de place : ", font=("", 16), borderwidth=0, relief='sunken')
        nbplace.grid(row=2, column=0)
        global comboboxu
        comboboxu = ttk.Combobox(nameframe, values=('1', '2', '3', '4', '5'), font=("", 16))
        comboboxu.grid(row=2, column=1)

        frame = LabelFrame(rootUser, font=("", 16), borderwidth=0, relief='sunken')
        frame.pack(pady=20, fill=BOTH)

        button = Button(frame, text="Back", font=("", 16), command=lambda: Save())
        button.pack(side=LEFT, padx=10, pady=10)

        button = Button(frame, text="Save", font=("", 16), command=lambda: Save())
        button.pack(side=RIGHT)

    def ShowReservation(name, surname, date1, date2, nb):
        print("##########################################################")
        print("#         Your reservation is ready                      #")
        print("#       Name : ", name)
        print("#       Surname : ", surname)
        print("#       Surname : ", surname)
        print("#       Departure : ", date1)
        print("#       Return : ", date2)
        print("#       Nb Place : ", nb)
        print("# Reservation Id : BOEING A385", random.randint(1, 200))

        print("################################################")

    def ShowInterfaceReservation(name, surname, dept, arr, nb,prix,date,date1):
        global recu
        reserve = Tk()
        reserve.title("Reçu reservation")
        reserve.geometry('610x450')

        frameR = LabelFrame(reserve, bg='white', font=("", 16), borderwidth=0, relief='sunken')
        frameR.pack(pady=20, fill=BOTH)

        recu = Label(frameR, font=("", 16))
        recu.pack(side=LEFT, fill=BOTH)

        a = random.randint(1,100)
        recu['text'] = ("##########################################################\n"
                       "#         Your reservation is ready                      #\n"
                       "#       Name : {}".format(name) + "\n"
                       "#       Surname : {}".format(surname) + "\n"
                       "#       Prix : {}".format(prix) + "\n"
                       "#       Departure : {}".format(dept) + "\n"
                       "#       Arrive : {}".format(arr) +"\n"
                       "#       Date departure : {}".format(date) + "\n"
                       "#       Date arrive : {}".format(date1) +"\n"
                       "#       Nb Place : {}".format(nb) +"\n"
                       "# Reservation Id : BOEING A385{}".format(a) +"\n"

                        "################################################\n")



    def Save():
        global nbplace
        global dept, arr, date, date1
        name = entryName.get()
        surname = entrySurname.get()
        nbplace = comboboxu.get()


        if utilisateur.IsUser(name)[0]:
            reservation.create_r(utilisateur.IsUser(name)[1]+1)
            vol.create_v(900,date,date1,1,2,1)


        else:
            u = utilisateur.create_u(name, surname)
            reservation.create_r(utilisateur.Id_u(name)+1)
            vol.create_v(900, date, date1, dept, arr, 1)

        ShowReservation(name, surname, dept, arr, nbplace)
        ShowInterfaceReservation(name,surname,dept,arr,nbplace,900,date,date1)

    def OngetNext():
        global dept, arr, date, date1
        dept = combobox.get()
        arr = combobox1.get()

        date = cal.get()
        date1 = cal2.get()
        root.destroy()
        print("A" + dept + arr + date + date1)

        InfoUser()

    b = Button(frame, text="Next", borderwidth=0, font=("", 16), background='dark green', relief='sunken')
    b.pack(side=BOTTOM)

    b['command'] = OngetNext

    root.mainloop()
