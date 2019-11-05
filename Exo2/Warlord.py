import random

class Warlord:

    def __init__(self, _x, _y):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 65
        self.speed = 30
        self.ac = 27

    def melee_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if ((d20 == 20) or (d20 == 19)):
                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,8) + 10)
            if (d20 + 20 > _ac):
                return (random.randint(1,8) + 10)

    def ranged_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (2*(random.randint(1,6) + 5))
            if (d20 + 19 > _ac):
                return (random.randint(1,6) + 5)