import random
from Mob import Mob

class Barbare(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 40, 17, 15, 110, 3, 3, "blue")
        self.life = (random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12)
        + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12)
        + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + 65)
        self.lifeMax=self.life

    def meleeAttack(self, _ac): # Renvoie les dégats que fait le barbare
        return(Mob.meleeAttack(self,_ac,19, 1, 8, 10, 3, 19))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if ((d20 == 20) or (d20 == 19)):
#                return (random.randint(1,8) + 10)
#            if (d20 + 19 > _ac):
#                return (3*(random.randint(1,8) + 10))#ça c'est bugué

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self,_ac, 19, 1, 8, 6, 3))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (3*(random.randint(1,8) + 6))
#            if (d20 + 19 > _ac):
#                return (random.randint(1,8) + 6)