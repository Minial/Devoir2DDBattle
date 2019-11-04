import random

class Warlord:

    def __init__(self, _x, _y):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 65
        self.speed = 30
        self.ac = 27
