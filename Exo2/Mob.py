#    def move(self):
#        if (self.position != self.destination):
#            dx = self.position[0] - self.destination[0]
#            dy = self.position[1] - self.destination[1]
#            l = np.sqrt(dx*dx + dy*dy)
#            px = dx*self.speed / l
#            py = dy*self.speed / l
#            if (self.speed > l):
#                self.position = self.destination
#            else :
#                if (self.terrain.constraint(self.position[0]-px, self.position[1]-py, self.size)):
#                    self.position = [self.position[0]-px, self.position[1]-py]
#                else :
#                    self.destination = self.position



#classe abstraite des différents mob,
#pour éviter d'avoir le meme code partout
import random
from random import *
import numpy as np


class Mob:
    def __init__(self, _x, _y, _la, _le, _size, _speed, _ac, _rangeMelee, _rangeRanged, _color):
        self.color = _color
        self.size = _size#diametre du mob
        self.position = [_x, _y]
        self.destination = self.position
        self.speed = _speed#vitesse du mob, aussi la distance max qu'il peut faire par tour
        self.ac = _ac
        self.listAllies = _la
        self.listEnnemie = _le
        self.rangeMelee = _rangeMelee
        self.rangeRanged = _rangeRanged
        self.listeDistanceEnnemie = []#stock les distances des différents ennemies
        self.idNearestEnnemie = []
        self.tourMob=False#le mob est en train de faire son tour
        self.canMeleeAttack=False#le mob peut taper melee
        self.canRangedAttack=False#le mob peut taper ranged
        #stocke par ordre croisant de distance les id des différents ennemis
        self.name=self.__class__.__name__#peut servir ou pas
        
        
    def meleeAttack(self, _ac, _taco, _diceNumber, _dicePower, _bonusDegat, _multiCrit=2, _critLuck=20):
        # Renvoie les dégats que fait le Mob
        d20 = random.randint(1,20)#jet de toucher du mob
        if (d20 == 1):#echec critique on touche jamais
            return 0
        else :
            degats=0#les dégats renvoyé
            if (d20 >= _critLuck):#critique ! on touche a coup sur avec double de dgt
                degats = _bonusDegat*_multiCrit
                for i in range (_diceNumber*_multiCrit):
                    degats=degats+random.randint(1,_dicePower)
            elif (d20 + _taco > _ac):
                degats = _bonusDegat
                for i in range (_diceNumber):
                    degats=degats+random.randint(1,_dicePower)
            #dans les autres cas on touche pas
            return degats
    
    def rangedAttack(self, _ac, _taco, _diceNumber, _dicePower, _bonusDegat, _multiCrit=2, _critLuck=20):
        # Renvoie les dégats que fait le Mob
        d20 = random.randint(1,20)#jet de toucher du mob
        if (d20 == 1):#echec critique on touche jamais
            return 0
        else :
            degats=0#les dégats renvoyé
            if (d20 >= _critLuck):#critique ! on touche a coup sur avec double de dgt
                degats = _bonusDegat*_multiCrit
                for i in range (_diceNumber*_multiCrit):
                    degats=degats+random.randint(1,_dicePower)
            elif (d20 + _taco > _ac):#attaque normal
                degats = _bonusDegat
                for i in range (_diceNumber):
                    degats=degats+random.randint(1,_dicePower)
            #dans les autres cas on touche pas
            return degats
        
    def observationDistanceEnnemie(self, posi=[]):
        if posi==[]:#position par defaut est notre position
            posi=self.position
        #par defaut par rapport a notre position actuelle
        self.listeDistanceEnnemie=len(self.listEnnemie)*[0]
        #permet de garder en mémoire la distance de toutles ennemies
        self.idNearestEnnemie = []
        for i in range(len(self.listEnnemie)): # Calcul des distance avec les ennemies
            dx = posi[0] - self.listEnnemie[i].position[0]
            dy = posi[1] - self.listEnnemie[i].position[1]
            distance = np.sqrt(dx*dx + dy*dy)
            self.listeDistanceEnnemie[i]=[distance- self.size/2 -self.listEnnemie[i].size/2, distance]
            j=0
            while (j<len(self.idNearestEnnemie) and self.listeDistanceEnnemie[i][0]>
                   self.listeDistanceEnnemie[self.idNearestEnnemie[j]][0]):
                j+=1
            self.idNearestEnnemie.insert(j,i)#on ordonne la liste des mobs par distance
    
    def deplacement(self, idMobVise):
        self.observationDistanceEnnemie()
        
        distance=self.listeDistanceEnnemie[idMobVise]#indique la distance du mob visé
        #en 0 c'est celle entre les bords des mobs et en 1 entre leur centre
        
        Xtotal = self.listEnnemie[idMobVise].position[0]- self.position[0]# selon thales c'est le X total
        Ytotal = self.listEnnemie[idMobVise].position[1]- self.position[1]
        l=distance[1]
        dep=distance[0]#pensez a soustraire distance attack
        if (dep <= self.rangeMelee): # Distance inférieur à l'attque melee on ne se déplace pas
            print("1")
            self.destination = self.position
            self.canMeleeAttack=True
            self.canRangedAttack=True
            print("le",self.name,"peut taper au cac sans deplacement")
            
        elif (dep <= self.speed + self.rangeMelee): # Déplacement en range melee (possibilité d'attaque)
            
            x = self.position[0] + (dep - self.rangeMelee)*Xtotal / l
            y = self.position[1] + (dep - self.rangeMelee)*Ytotal / l
            self.destination = [x,y]
            self.canMeleeAttack=True
            self.canRangedAttack=True
            print("le",self.name,"peut taper cac avec deplacement")

        elif (dep <= self.speed + self.rangeRanged): # Déplacement en range distance (possibilité d'attaque)
            x = self.position[0] + (dep - self.rangeRanged)*Xtotal / l
            y = self.position[1] + (dep - self.rangeRanged)*Ytotal / l
            self.destination = [x,y]
            self.canMeleeAttack=False
            self.canRangedAttack=True
            print("le",self.name,"peut taper distance avec deplacement")

        elif (dep <= 2*self.speed + self.rangeMelee): # Déplacement en range melee (impossible d'attaquer)
            x = self.position[0] + (dep - self.rangeMelee)*Xtotal / l
            y = self.position[1] + (dep - self.rangeMelee)*Ytotal / l
            self.destination = [x,y]
            print("le",self.name,"peut pas taper cac avec deplacement")

        elif (dep <= 2*self.speed + self.rangeRanged): # Déplacement en range distance (impossible d'attaquer)
            x = self.position[0] + (dep - self.rangeRanged)*Xtotal / l
            y = self.position[1] + (dep - self.rangeRanged)*Ytotal / l
            self.destination = [x,y]
            print("le",self.name,"peut pas taper distance avec deplacement")

        else : # Déplacement max
            print("6")
            x = self.position[0] + 2*self.speed*Xtotal/l
            y = self.position[0] + 2*self.speed*Ytotal/l
            self.destination = [x,y]
            print("le",self.name,"peut pas taper avec deplacement")

        print(self.destination)


    def deltaAction(self):
        if (self.position != self.destination):
            dx = self.position[0] - self.destination[0]
            dy = self.position[1] - self.destination[1]
            l = np.sqrt(dx*dx + dy*dy)
            px = dx*self.speed/10 / l
            py = dy*self.speed/10 / l
            if (self.speed/10 > l):
                self.position = self.destination
                self.tourMob = False
            else :
                self.position = [self.position[0]-px, self.position[1]-py]

        #else:
        #    if (self.canMeleeAttack):
        #        self.listEnnemie[id].life = self.listEnnemie[id].life - meleeAttack(self.listEnnemie[id].ac)
        #    elif (self.canRangedAttack):
        #        self.listEnnemie[id].life = self.listEnnemie[id].life - rangedAttack(self.listEnnemie[id].ac)
        #    self.tourMob = False
