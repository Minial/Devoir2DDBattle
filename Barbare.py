import random

class Barbare:

    def __init__(self, _x, _y):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + random.randint(1,12) + 65
        self.speed = 40
        self.ac = 17
