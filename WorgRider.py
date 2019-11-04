import random

class WorgRider:

    def __init__(self, _x, _y):
        self.size = 15
        self.position = [_x, _y]
        self.life = random.randint(1,10) + random.randint(1,10) + 2
        self.speed = 20
        self.ac = 18

