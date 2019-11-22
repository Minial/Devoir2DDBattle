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
        self.tourvar = False
        self.listeMobs = []#tout le monde !
        self.listeGentils = []#les gentils !
        self.listeMéchants = []#les vilains pas bô
        self.listeMobs.append(Solar(500,750,self.listeGentils,self.listeMéchants))
        self.listeGentils.append(self.listeMobs[0])
        print ("Prenez garde au solaire avec ses",self.listeMobs[0].life,"PV !")
        self.summonWorgRider(9)
        self.summonWarLord(1)
        self.summonBarbare(4)
    
    
    def summonWorgRider(self,number):#on invoque un nombre number de WorgRider
        for i in range(number):
            listeCoord=self.distance(15)
            self.listeMobs.append(WorgRider(listeCoord[0],listeCoord[1],self.listeMéchants,self.listeGentils))
            self.listeMéchants.append(self.listeMobs[len(self.listeMobs)-1])#on ajoute mob dans liste méchant
            print ("je suis un WorgRider avec",self.listeMobs[len(self.listeMobs)-1].life)
            
    def summonWarLord(self,number):#on invoque un nombre number de warlord
        for i in range(number):
            listeCoord=self.distance(15)
            self.listeMobs.append(Warlord(listeCoord[0],listeCoord[1],self.listeMéchants,self.listeGentils))
            self.listeMéchants.append(self.listeMobs[len(self.listeMobs)-1])#on ajoute mob dans liste méchant
            print ("je suis un Warlord avec",self.listeMobs[len(self.listeMobs)-1].life)
    
    def summonBarbare(self,number):#on invoque un nombre number de warlord
        for i in range(number):
            listeCoord=self.distance(15)
            self.listeMobs.append(Barbare(listeCoord[0],listeCoord[1],self.listeMéchants,self.listeGentils))
            self.listeMéchants.append(self.listeMobs[len(self.listeMobs)-1])#on ajoute mob dans liste méchant
            print ("je suis un Barbare avec",self.listeMobs[len(self.listeMobs)-1].life)
        
    
    # 9 au premier fight
    def distance(self, size):#calcule la positon pour invoquer un nouvelle ennemi qui ne rentre pas dans un autre
        chevauchement=True
        while chevauchement:
            listeCoord=[500+randint(-250,250),750+randint(-100,100)]
            chevauchement=False
            for mob in self.listeMobs:
                dx=mob.position[0]-listeCoord[0]
                dy=mob.position[1]-listeCoord[1]
                distance=sqrt(dx**2+dy**2)
                if(distance<=mob.size+size):#le size du nouveau mob
                    chevauchement=True
        return listeCoord
        
    def tour(self):#le mob se tape lui-même
        self.listeMobs[0].life=self.listeMobs[0].life-self.listeMobs[0].meleeAttack(18)
        self.listeMobs[0].position[0]=self.listeMobs[0].position[0]+10
        print (self.listeMobs[0].life)
        for mob in self.listeMobs:
            if mob.life<=0 :
                print("il est mort !")
                del self.listeMobs[self.listeMobs.index(mob)]
            else:
                print("invaincu !")

    def tour2(self):
        for i in range(len(self.listeMobs)):
            self.listeMobs[i].tourMob = True
        self.tourvar = True
        self.listeMobs[0].deplacement(9)
        self.listeMobs[10].deplacement(0)


    def action(self):
        if (self.tourvar):
            i=0
            while(i<len(self.listeMobs)):
                if (not(self.listeMobs[i].tourMob)):
                    i=i+1
                else :
                    self.listeMobs[i].deltaAction()
                    return 0
        self.tourvar = False
    
terr=Terrain()
terr.listeMobs[0].observationDistanceEnnemie()
terr.listeMobs[0].deplacement(0)