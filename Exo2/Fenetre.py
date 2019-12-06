from tkinter import *
import numpy as np

from Mob import Mob
from WorgRider import WorgRider
from Solar import Solar
from Warlord import Warlord
from Barbare import Barbare
from Terrain import Terrain

# ###
# Constante
terrain = Terrain()
time=3
w=terrain.tailleX
h=terrain.tailleY

# ###
# Affichage de la fenetre
def affiche_fenetre():
    global fenetre, canvas
    
    fenetre = Tk()
    fenetre.title('Dongeons et Dragons')

    fenetre.resizable(False,False)

    fenetre.after(time, affichage)
    
    canvas = Canvas(fenetre, width=w, height=h, background='white')
    canvas.pack(side=LEFT)
    bouttonTour = Button(fenetre, text ='Tour', command=terrain.tour2)
    bouttonTour.pack(side=RIGHT, padx=10, pady=10)

    affiche_jeu()
    fenetre.mainloop()
    
# ###
# Affichage du plateau de jeu
def affiche_jeu():
    global terrain
    canvas.delete(ALL)
    for i in range(len(terrain.listeMobs)):
        if (terrain.listeMobs[i].life > 0):
            canvas.create_oval(np.round(terrain.listeMobs[i].position[0] - terrain.listeMobs[i].size),
                            np.round(terrain.listeMobs[i].position[1] - terrain.listeMobs[i].size),
                            np.round(terrain.listeMobs[i].position[0] + terrain.listeMobs[i].size),
                            np.round(terrain.listeMobs[i].position[1] + terrain.listeMobs[i].size),
                            fill=terrain.listeMobs[i].color)

def etatProchain():
    terrain.action()


# ###
# Boucle d'affichage du jeu
def affichage():
    etatProchain()
    affiche_jeu()
    fenetre.after(time,affichage)

# ###
# Début
affiche_fenetre()