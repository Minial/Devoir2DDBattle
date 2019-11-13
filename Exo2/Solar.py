import random
import numpy as np
from Mob import Mob

class Solar(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 30, 150, 44, 30, 330)
        self.destination = self.position
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 242
        self.lifeMax=self.life#pour éviter de soigner un mob de plus que son max

    def melee_attack(self, _ac): # Renvoie les dégats que fait le Solar
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (2*(random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18))
            if (d20 + 35 > _ac):
                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18)

    def ranged_attack(self, _ac): # Renvoie les dégats que fait le Solar
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (2*(random.randint(1,6) + random.randint(1,6) + 14))
            if (d20 + 31 > _ac):
                return (random.randint(1,6) + random.randint(1,6) + 14)

    def action(self):
        listeDistance = []
        for i in range(len(self.listEnnemie)): # Calcul des distance avec les ennemies
            dx = self.position[0] - self.listEnnemie[i].position[0]
            dy = self.position[1] - self.listEnnemie[i].position[1]
            l = np.sqrt(dx*dx + dy*dy)
            listeDistance.append([l - self.size/2 -self.listEnnemie[i].size/2, l])

        minDist = min(listeDistance) # Distance minimum

        if (minDist[0] <= self.rangeMelee): # Distance inférieur à l'attque melee on ne se déplace pas
            destination = self.position
            
        elif (minDist[0] <= self.speed + self.rangeMelee): # Déplacement en range melee (possibilité d'attaque)
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]

        elif (minDist[0] <= self.speed + self.rangeRanged): # Déplacement en range distance (possibilité d'attaque)
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeRanged)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeRanged)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]

        elif (minDist[0] <= 2*self.speed + self.rangeMelee): # Déplacement en range melee (impossible d'attaquer)
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]

        elif (minDist[0] <= 2*self.speed + self.rangeRanged): # Déplacement en range distance (impossible d'attaquer)
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]

        else : # Déplacement max
            x = 2*self.speed*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0])/minDist[1]
            y = 2*self.speed*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1])/minDist[1]
            destination = [x,y]