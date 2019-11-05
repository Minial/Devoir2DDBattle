import random

class WorgRider:

    def __init__(self, _x, _y):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,10) + random.randint(1,10) + 2
        self.speed = 20
        self.ac = 18

    def melee_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (3*(random.randint(1,8) + 2))
            if (d20 + 6 > _ac):
                return (random.randint(1,8) + 2)

    def ranged_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if (d20 == 20):
                return (3*(random.randint(1,6)))
            if (d20 + 4 > _ac):
                return (random.randint(1,6))
