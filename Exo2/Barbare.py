import random
from Mob import Mob

class Barbare:

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 15, 40, 17, 30, 330)
        self.life = random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + 65
        self.lifeMax=self.life

    def melee_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if ((d20 == 20) or (d20 == 19)):
                return (random.randint(1,8) + 10)
            if (d20 + 19 > _ac):
                return (3*(random.randint(1,8) + 10))

    def ranged_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (3*(random.randint(1,8) + 6))
            if (d20 + 19 > _ac):
                return (random.randint(1,8) + 6)