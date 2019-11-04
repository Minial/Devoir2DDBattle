import random

class Solar:

    def __init__(self, _x, _y):
        self.size = 30
        self.position = [_x, _y]
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 242
        self.speed = 150
        self.ac = 44
        self.regen = 15 

    def melee_attack(self, _ac):
        d20 = random.randint(1,20)
        if (d20 == 1):
            return 0
        else :
            if ((d20 + 35 > _ac) or (d20 == 20)):
                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18)
