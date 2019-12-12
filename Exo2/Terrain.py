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
        self.listeAttaque = []#attaque du tour
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
            listeCoord=[500+randint(-250,250),250+randint(-100,100)]
            chevauchement=False
            for mob in self.listeMobs:
                dx=mob.position[0]-listeCoord[0]
                dy=mob.position[1]-listeCoord[1]
                distance=sqrt(dx**2+dy**2)
                if(distance<=mob.size+size):#le size du nouveau mob
                    chevauchement=True
        return listeCoord
        
    def tour3(self):
        for i in range(len(self.listeMobs)):
            self.listeMobs[i].tourMob = True
        self.tourvar = True
        #init tour
        i=0
        nombreMobs=len(self.listeMobs)
        while i<nombreMobs:
        #for i in range(len(self.listeMobs)):
            self.listeMobs[i].hardIA()
            cadavre=self.nettoyageCadavre(i)
            i=i+1-cadavre[0]
            nombreMobs=len(self.listeMobs)
        print ("==========fin tour==========")

    def nettoyageCadavre(self,index):
        numberMobs=len(self.listeMobs)
        i=0
        cadavre=[0,0]
        toremove=[]
        while i<numberMobs:
            if (self.listeMobs[i].life<=0):
                #self.listeMobs.remove(self.listeMobs[i])
                toremove.append(self.listeMobs[i])
                #cadavre+=1
                if (i<index):
                    cadavre[0]+=1
                elif(i>index):
                    cadavre[1]+=1
                #else:
                    #nothing
            i+=1
        for i in range (len(toremove)):
            self.listeMobs.remove(toremove[i])
        return cadavre
    

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
        #print("tour fini")
        
    def tour2(self):
        for i in range(len(self.listeMobs)):
            self.listeMobs[i].tourMob = True
        self.tourvar = True
        for i in range(len(self.listeMobs)):
            if (i == 0):
                self.listeMobs[i].deplacement(9)
            else :
                self.listeMobs[i].deplacement(0)
    
#terr=Terrain()
#terr.listeMobs[0].observationDistanceEnnemie()
#terr.listeMobs[0].deplacement(0)