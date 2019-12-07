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
import webbrowser

from math import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from bs4 import BeautifulSoup
from liste_sorts import get_all_spells
from liste_sorts import getUrlSpell
from liste_sorts import get_all_creatures
from index_inverse import index_inverse




liste_sorts = get_all_spells()
liste_sorts.sort()



def clic(evt):
    i=li.curselection()
    sort = li.get(i)
    lc.delete("0","end")
    liste_creatures = index_inverse(sort)
    liste_creatures.sort()
    for j in range(0,len(liste_creatures)):
        lc.insert("end",liste_creatures[j])
    return sort
    
def openweb():
    i=li.curselection()
    sort = li.get(i)
    url = getUrlSpell(sort)
    webbrowser.open(url)


def inverse_sens_CS():
    fen2 = Toplevel()
    fen2.geometry("500x500+100+100")
    fen2.title("Page d'accueil")
    Titre= LabelFrame(fen2, padx=15, pady=15, bg='#ffffff')
    Titre.pack(expand="yes")

    Label(Titre, text="Recherche créatures et sorts", bg="#ffffff", font=("Helvetica 15 bold")).pack()
     
    Label(fen2, text= "Nom de la créature :").pack()


    #Premiere liste comportant les sorts
    li = tk.Listbox(fen2)
    for i in range(0,len(liste_creatures)):
        li.insert("end",liste_creatures[i])
    li.pack()

    #methode pour retourner le sort cliqué
    li.bind('<ButtonRelease-1>',clic2)


    Label(fen2, text= " ", font=("Helvetica", 12)).pack()
    Label(fen2, text= "Noms des créatures ayant ce sort :").pack()

    #Liste comportant les créatures
    lc = tk.Listbox(fen2)
    lc.pack()

    Label(fen2, text= " ", font=("Helvetica", 12)).pack()
    
    
    
    
    
    


#MAIN

#fenetre principale sorts -> créatures
fen1 = Tk()
fen1.geometry("500x500+100+100")
fen1.title("Page d'accueil")


Titre= LabelFrame(fen1, padx=15, pady=15, bg='#ffffff')
Titre.pack(expand="yes")


Label(Titre, text="Recherche créatures et sorts", bg="#ffffff", font=("Helvetica 15 bold")).pack()

Button(fen1, text="Recherche créature -> sorts", command=inverse_sens_CS).pack()      
      
Label(fen1, text= "Nom du sort :").pack()


#Premiere liste comportant les sorts
li = tk.Listbox(fen1)
for i in range(0,len(liste_sorts)):
    li.insert("end",liste_sorts[i])
li.pack()

Button(fen1, text="Lien vers la page web du sort", command=openweb).pack()

#methode pour retourner le sort cliqué
li.bind('<ButtonRelease-1>',clic)


Label(fen1, text= " ", font=("Helvetica", 12)).pack()
Label(fen1, text= "Noms des créatures ayant ce sort :").pack()

#Liste comportant les créatures
lc = tk.Listbox(fen1)
lc.pack()

Label(fen1, text= " ", font=("Helvetica", 12)).pack()

fen1.mainloop()





