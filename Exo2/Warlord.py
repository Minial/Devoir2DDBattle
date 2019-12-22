import random
from Mob import Mob

class Warlord(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 30, 27, 15, 25, 3, 1, "red")
        self.life = (random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + 65)
        self.lifeMax=self.life
        self.will = 6


    def meleeAttack(self, _ac): # Renvoie les dégats que fait le Warlord
        return(Mob.meleeAttack(self,_ac,20, 1, 8, 10, 3, 19))

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self,_ac, 19, 1, 6, 5))
