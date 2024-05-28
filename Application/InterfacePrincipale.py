from calendar import calendar
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar


import tkinter.messagebox

import sys

import calendar
from sqlalchemy import false, true

root = Tk()
root.geometry('700x600')
root.title('Gestion de Compagnie Aérienne')

frame = LabelFrame(root,text="      BIENVENUE SUR LA PAGE DE RESERVATION DES VOLS",bg='white',font=("",16),borderwidth=0,relief='sunken')
frame.pack(pady=50,fill=BOTH)

frame1 = LabelFrame(frame,bg='white',font=("",16),borderwidth=0,relief='sunken')
frame1.pack(pady=150,fill=BOTH,expand=True)

label = Label(frame1,text="Pays de départ : ",font=("",12))
label.grid(row=0,column=0)

label1 = Label(frame1,text="  Pays de destination : ",font=("",12))
label1.grid(row=0,column=2)

combobox = ttk.Combobox(frame1,values=('B','C','D','E','F','G','H'),font=("",12))
combobox.grid(row=0,column=1)

combobox1 = ttk.Combobox(frame1,values=('B','C','D','E','F','G','H'),font=("",12))
combobox1.grid(row=0,column=3)

label_c = Label(frame1)
label_c.grid(row=1,column=0)

c = Calendar(label_c,selectmode='day')
#c.pack(padx=1,pady=1)








root.mainloop()