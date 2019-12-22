import random
from Mob import Mob

class Barbare(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 40, 17, 15, 110, 3, 3, "blue")
        self.life = (random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12)
        + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12)
        + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + 65)
        self.lifeMax=self.life
        self.will = 9

    def meleeAttack(self, _ac): # Renvoie les dégats que fait le barbare
        return(Mob.meleeAttack(self,_ac,19, 1, 8, 10, 3, 19))

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self,_ac, 19, 1, 8, 6, 3))
