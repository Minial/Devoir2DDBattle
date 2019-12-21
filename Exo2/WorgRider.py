import random
from Mob import Mob

class WorgRider(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 20, 18, 15, 60, 1, 1, "black")
        self.life = random.randint(1,10) + random.randint(1,10) + 2
        self.lifeMax=self.life

    def meleeAttack(self, _ac): # Renvoie les dégats que fait le WorgRider
        return(Mob.meleeAttack(self,_ac,6, 1, 8, 2, 3))

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self, _ac, 4, 1, 6, 0, 3))

