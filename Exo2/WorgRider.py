import random
from Mob import Mob

class WorgRider(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 20, 18, 15, 60, 1, 1, "black")
        self.life = random.randint(1,10) + random.randint(1,10) + 2
        self.lifeMax=self.life

    def meleeAttack(self, _ac): # Renvoie les dégats que fait le WorgRider
        return(Mob.meleeAttack(self,_ac,6, 1, 8, 2, 3))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (3*(random.randint(1,8) + 2))
#            if (d20 + 6 > _ac):
#                return (random.randint(1,8) + 2)

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self, _ac, 4, 1, 6, 0, 3))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (3*(random.randint(1,6)))
#            if (d20 + 4 > _ac):
#                return (random.randint(1,6))
