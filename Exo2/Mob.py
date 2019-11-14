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
from numpy import *


class Mob:
    def __init__(self, _x, _y, _la, _le, _size, _speed, _ac, _rangeMelee, _rangeRanged, _color):
        self.color = _color
        self.size = _size#diametre du mob
        self.position = [_x, _y]
        self.speed = _speed
        self.ac = _ac
        self.listAllies = _la
        self.listEnnemie = _le
        self.rangeMelee = _rangeMelee
        self.rangeRanged = _rangeRanged
        self.listeDistanceEnnemie = []#stock les distances des différents ennemies
        self.idNearestEnnemie = []
        #stocke par ordre croisant de distance les id des différents ennemis
        
        
    def meleeAttack(self, _ac, _taco, _diceNumber, _dicePower, _bonusDegat, _multiCrit=2, _critLuck=20): # Renvoie les dégats que fait le Mob
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
    
    def rangedAttack(self, _ac, _taco, _diceNumber, _dicePower, _bonusDegat, _multiCrit=2, _critLuck=20): # Renvoie les dégats que fait le Mob
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
        
    def observationDistanceEnnemie(self):
        self.listeDistanceEnnemie=len(self.listEnnemie)*[0]#permet de garder en mémoire la distance de tout les ennemies
        for i in range(len(self.listEnnemie)): # Calcul des distance avec les ennemies
            dx = self.position[0] - self.listEnnemie[i].position[0]
            dy = self.position[1] - self.listEnnemie[i].position[1]
            distance = sqrt(dx*dx + dy*dy)
            self.listeDistanceEnnemie[i]=distance- self.size/2 -self.listEnnemie[i].size/2