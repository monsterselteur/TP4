from calendar import calendar
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry

from DAO import pays


import tkinter.messagebox

import sys

import calendar
from sqlalchemy import false, true
def interfacePrincipale():
    root = Tk()
    root.geometry('600x400')
    root.title('Gestion de Compagnie Aérienne')

    frame = LabelFrame(root,text="      BIENVENUE SUR LA PAGE DE RESERVATION DES VOLS",bg='white',font=("",16),borderwidth=0,relief='sunken')
    frame.pack(pady=50,fill=BOTH)

    frame1 = LabelFrame(frame,bg='white',font=("",16),borderwidth=0,relief='sunken')
    frame1.pack(pady=40,fill=BOTH,expand=True)

    label = Label(frame1,text="       Pays de départ : ",font=("",16),borderwidth=5,padx=10,relief='sunken')
    label.grid(row=0,column=0)

    label1 = Label(frame1,text="Pays de destination : ",font=("",16),borderwidth=5,padx=10,relief='sunken')
    label1.grid(row=1,column=0)

    combobox = ttk.Combobox(frame1,values=(pays.read_all_p()),font=("",16))
    combobox.grid(row=0,column=1)

    combobox1 = ttk.Combobox(frame1,values=(pays.read_all_p()),font=("",16))
    combobox1.grid(row=1,column=1)

    cal = DateEntry(frame1,font=("",16),selectionmode='date',borderwidth=20,padx=10,relief='sunken')
    cal.grid(row=2,column=1)
    cal2 = DateEntry(frame1,font=("",16),selectionmode='date',borderwidth=20,padx=10,relief='sunken')
    cal2.grid(row=3,column=1)

    label2 = Label(frame1,text="    Date de depart     : ",font=("",16),borderwidth=5,padx=10,relief='sunken')
    label2.grid(row=2,column=0)

    label3 = Label(frame1,text="    Date de retour      : ",font=("",16),borderwidth=5,padx=10,relief='sunken')
    label3.grid(row=3,column=0)

    def InfoUser():
        rootUser = Tk()
        rootUser.geometry('610x450')
        rootUser.title("User information")

        nameframe = LabelFrame(rootUser,text='              User Information \n\n',font=("",16),borderwidth=0,relief='sunken')
        nameframe.pack(pady=20,fill=BOTH)

        labelName = Label(nameframe,text="              \n\nNom : ",font=("",16),borderwidth=0,relief='sunken')
        labelName.grid(row=0,column=0)

        labelSurname = Label(nameframe, text="      \n\nSurname : \n\n", font=("", 16), borderwidth=0, relief='sunken')
        labelSurname.grid(row=1, column=0)

        entrySurname = Entry(nameframe,font=("",16))
        entryName = Entry(nameframe,font=("",16))

        entrySurname.grid(row=1, column=1)
        entryName.grid(row=0, column=1)

        nbplace = Label(nameframe,text="Nombre de place : ",font=("",16),borderwidth=0,relief='sunken')
        nbplace.grid(row=2,column=0)

        combobox1 = ttk.Combobox(nameframe, values=('1', '2', '3', '4', '5'), font=("", 16))
        combobox1.grid(row=2, column=1)

        frame = LabelFrame(rootUser,font=("",16),borderwidth=0,relief='sunken')
        frame.pack(pady=20,fill=BOTH)

        button = Button(frame, text="Back", font=("", 16), command=lambda: Save())
        button.pack(side=LEFT,padx=10,pady=10)

        button = Button(frame, text="Save", font=("", 16), command=lambda: Save())
        button.pack(side=RIGHT)

    def Save():
        pass

    def OngetNext():
        dept = combobox.get()
        arr = combobox1.get()

        date = cal.get()
        date1 = cal2.get()
        root.destroy()
        print("A" + dept+arr+date+date1)

        InfoUser()


    b =Button(frame,text="Next",borderwidth=0,font=("",16),background='dark green',relief='sunken')
    b.pack(side=BOTTOM)

    b['command']=OngetNext

    root.mainloop()