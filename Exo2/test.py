import numpy as np


def deltaAction(self):
    if (self.position != self.destination):
        dx = self.position[0] - self.destination[0]
        dy = self.position[1] - self.destination[1]
        l = np.sqrt(dx*dx + dy*dy)
        px = dx*self.speed / l
        py = dy*self.speed / l
        if (self.speed/100 > l):
            self.position = self.destination
        else :
            self.position = [self.position[0]-px, self.position[1]-py]

    else:
        if (self.attackMelee):
            self.listEnnemie[id].life = self.listEnnemie[id].life - meleeAttack(self.listEnnemie[id].ac)
        elif (self.attackRange):
            self.listEnnemie[id].life = self.listEnnemie[id].life - rangedAttack(self.listEnnemie[id].ac)
        self.tourMob = False


def action(self):
    if (self.tour):
        i=0
        if (i<len(self.listeMobs)):
            while(not(self.listeMobs[i].tourMob)):
                i=i+1
            self.liseMob[i].deltaAction()
    self.tour = False


def etatProchain():
    terrain.action()