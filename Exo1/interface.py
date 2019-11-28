#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:10:27 2019

@author: samuelogier
"""
import os
import csv
import random
import math
import tkinter.font as tkFont
import tkinter as tk
import pymongo

from math import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from bs4 import BeautifulSoup
from liste_sorts import get_all_spells




liste_sorts = get_all_spells()
liste_sorts.sort()

#MAIN

#fenetre principale
fen1 = Tk()
fen1.geometry("500x370+100+100")
fen1.title("Page d'accueil")

Titre= LabelFrame(fen1, padx=15, pady=15, bg='#ffffff')
Titre.pack(expand="yes")

Label(Titre, text="Recherche créatures et sorts", bg="#ffffff", font=("Helvetica 15 bold")).pack()

Label(fen1, text= "Nom du sort :").pack()
"""maZone = Entry(fen1, width=30)
maZone.pack()
maZone.get()"""

li = tk.Listbox(fen1)
for i in range(0,len(liste_sorts)):
    li.insert("end",liste_sorts[i])
li.pack()


Button(fen1, text = "Rechercher").pack()

Label(fen1, text= " ", font=("Helvetica", 12)).pack()

fen1.mainloop()










