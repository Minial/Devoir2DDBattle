"""
Created on Mon Nov  4 14:27:38 2019

@author: adrien
"""

#link : https://docs.google.com/document/d/12GTrjIkMww9EiQ0zGA33QFkvUQD_FiimGRWDcZ0vOtM/edit#

from random import *
from numpy import *

from WorgRider import WorgRider # 9 au premier fight
from Solar import Solar
from Warlord import Warlord # 1
from Barbare import Barbare # 4

class Terrain :
    tailleX = 1000
    tailleY = 1000
    #id = -1 #sert pour l'identification d'un mob
    
    def __init__(self):
        self.listeMobs = []
        self.listeMobs.append(Solar(500,250))
        for i in range(9):
            listeCoord=self.distance()
            self.listeMobs.append(WorgRider(listeCoord[0],listeCoord[1]))
            print (self.listeMobs[i+1].life)
        print (self.listeMobs[0].life)
        
    def distance(self):
        chevauchement=True
        while chevauchement:
            listeCoord=[500+randint(-250,250),750+randint(-100,100)]
            chevauchement=False
            for mob in self.listeMobs:
                dx=mob.position[0]-listeCoord[0]
                dy=mob.position[1]-listeCoord[1]
                distance=sqrt(dx**2+dy**2)
                if(distance<=15):
                    chevauchement=True;
        return listeCoord
        
    def Tour(self):
        self.listeMobs[0].life=self.listeMobs[0].life-100
        print (self.listeMobs[0].life)
        for mob in self.listeMobs:
            if mob.life<=0 :
                print("il est mort !")
                del self.listeMobs[self.listeMobs.index(mob)]
            else:
                print("invaincu !")
    
