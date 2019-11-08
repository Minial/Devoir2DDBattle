import random
import numpy as np

class Solar:

    def __init__(self, _x, _y, _la, _le):
        self.size = 30
        self.position = [_x, _y]
        self.destination = self.position
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 242
        self.speed = 150
        self.ac = 44
        self.rangeMelee = 30
        self.rangeRanged = 330
        self.listAllies = _la
        self.listEnnemie = _le

    def melee_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (2*(random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18))
            if (d20 + 35 > _ac):
                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18)

    def ranged_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (2*(random.randint(1,6) + random.randint(1,6) + 14))
            if (d20 + 31 > _ac):
                return (random.randint(1,6) + random.randint(1,6) + 14)

    def action(self, _listeMob):
        listeDistance = []
        for i in range(len(_listeMob)):
            dx = self.position[0] - _listeMob[i].position[0]
            dy = self.position[1] - _listeMob[i].position[1]
            l = np.sqrt(dx*dx + dy*dy)
            listeDistance.append([l - self.size/2 -_listeMob[i].size/2, l])

        minDist = min(listeDistance)
        if (minDist[0] <= self.rangeMelee):
            destination = self.position
            
        elif (minDist[0] <= self.speed + self.rangeMelee):
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]
        elif (minDist[0] <= self.speed + self.rangeRanged):
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeRanged)*(_listeMob(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeRanged)*(_listeMob(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]
        elif (minDist[0] <= 2*self.speed + self.rangeMelee):
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]
        elif (minDist[0] <= 2*self.speed + self.rangeRanged):
            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(_listeMob(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
            destination = [x,y]
        else :
            x = 2*self.speed*(_listeMob(listeDistance.index(minDist)).position[0] - self.position[0])/minDist[1]
            y = 2*self.speed*(_listeMob(listeDistance.index(minDist)).position[1] - self.position[1])/minDist[1]
            destination = [x,y]