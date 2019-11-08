import random

class Barbare:

    def __init__(self, _x, _y, _la, _le):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + 65
        self.speed = 40
        self.ac = 17
        self.listAllies = _la
        self.listEnnemie = _le

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