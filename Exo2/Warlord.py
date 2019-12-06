import random
from Mob import Mob

class Warlord(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 30, 27, 15, 25, 3, 1, "red")
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + 65
        self.lifeMax=self.life


    def meleeAttack(self, _ac): # Renvoie les dégats que fait le Warlord
        return(Mob.meleeAttack(self,_ac,20, 1, 8, 10, 3, 19))
        #normalement il a un bonus de 2d6 mais j'ai  modifié le multiplicateur, c'est plus simple
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if ((d20 == 20) or (d20 == 19)):
#                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,8) + 10)
#            if (d20 + 20 > _ac):
#                return (random.randint(1,8) + 10)

    def rangedAttack(self, _ac):
        return(Mob.rangedAttack(self,_ac, 19, 1, 6, 5))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (2*(random.randint(1,6) + 5))
#            if (d20 + 19 > _ac):
#                return (random.randint(1,6) + 5)