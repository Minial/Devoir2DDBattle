import random
import numpy as np
from Mob import Mob

class Solar(Mob):

    def __init__(self, _x, _y, _la, _le):
        Mob.__init__(self, _x, _y, _la, _le, 30, 150, 44, 30, 330, 4, 4, "yellow")
        self.life = random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
        + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 242
        self.lifeMax=self.life#pour éviter de soigner un mob de plus que son max

    def meleeAttack(self, _ac): # Renvoie les dégats que fait le Solar
        return(Mob.meleeAttack(self,_ac,35, 3, 6, 18))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (2*(random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18))
#            if (d20 + 35 > _ac):
#                return (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 18)

    def rangedAttack(self, _ac): # Renvoie les dégats que fait le Solar
        return(Mob.rangedAttack(self,_ac, 31, 2, 6, 14))
#        d20 = random.randint(1,20)
#        if (d20 == 1):
#            return 0
#        else :
#            if (d20 == 20):
#                return (2*(random.randint(1,6) + random.randint(1,6) + 14))
#            if (d20 + 31 > _ac):
#                return (random.randint(1,6) + random.randint(1,6) + 14)

#    def action(self):
#        #indique la destination et le type d'attaque possible
#        listeDistance = []
#        for i in range(len(self.listEnnemie)): # Calcul des distance avec les ennemies
#            dx = self.position[0] - self.listEnnemie[i].position[0]
#            dy = self.position[1] - self.listEnnemie[i].position[1]
#            l = np.sqrt(dx*dx + dy*dy)
#            listeDistance.append([l - self.size/2 -self.listEnnemie[i].size/2, l])
#
#        minDist = min(listeDistance) # Distance minimum
#
#        if (minDist[0] <= self.rangeMelee): # Distance inférieur à l'attque melee on ne se déplace pas
#           self.destination = self.position
#            
#        elif (minDist[0] <= self.speed + self.rangeMelee): # Déplacement en range melee (possibilité d'attaque)
#            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
#            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
#            self.destination = [x,y]
#
#        elif (minDist[0] <= self.speed + self.rangeRanged): # Déplacement en range distance (possibilité d'attaque)
#            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeRanged)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
#            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeRanged)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
#            self.destination = [x,y]
#
#        elif (minDist[0] <= 2*self.speed + self.rangeMelee): # Déplacement en range melee (impossible d'attaquer)
#            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
#            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
#            self.destination = [x,y]
#
#        elif (minDist[0] <= 2*self.speed + self.rangeRanged): # Déplacement en range distance (impossible d'attaquer)
#            x = self.position[0] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0]) / minDist[1]
#            y = self.position[1] + (minDist[0] + self.size/2 - self.rangeMelee)*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1]) / minDist[1]
#            self.destination = [x,y]
#
#        else : # Déplacement max
#            x = 2*self.speed*(self.listEnnemie(listeDistance.index(minDist)).position[0] - self.position[0])/minDist[1]
#            y = 2*self.speed*(self.listEnnemie(listeDistance.index(minDist)).position[1] - self.position[1])/minDist[1]
#            self.destination = [x,y]
    
    def IADecision(self, rayon, angle, action, cible1, cible2, cible3, cible4):
        #chaque param est entre 0 et 1 et sera remis dans l'intervarlle utile plus loin
        #l'ia vas donner pour se deplacer une position angulaire (entre 0 et 1 pour chaque, a transposer ensuite)
        #elle vas aussi donner l'action, entre 0 et 1, avec entre >1/3 deplacement doublé
        #1/3<x<2/3 attaque melee et >2/3 attaque ranged (possibilité ajout action)
        #cibleX est la cible pour l'attaque numero X du monstre s'il attaque
        #4 cible, car il peut taper 4 mob max
        nombreAction=3#permet de donner le nombre d'action différente possible par le mob
        mouvX=rayon*self.speed*np.cos(angle*360)#deplacement selon X
        mouvY=rayon*self.speed*np.sin(angle*360)#deplacement selon Y
        self.destination=[self.position[0]+mouvX,self.position[1]+mouvY]
        self.observationDistanceEnnemie(self.destination)
        #on regarde la distance des mobs par rapport a notre position fin de tour
        if action<1/nombreAction :#cas deplacement double distance
            self.destination=[self.position[0]+2*mouvX,self.position[1]+2*mouvY]
            return "Deplacement"
        elif action<2/nombreAction:#attaque melee
            self.observationDistanceEnnemie(self)#permet d'avoir en memoire distance des mobs (ou actualiser)
            degat=[]#chaque case contient 2 case, l'id de la cible, et les dégats qu'elle prend
            cible=round(cible1*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeMelee :#on vérifie si on peut taper le mob
                degat.append[cible, self.meleeAttack(self.listEnnemie[cible].ac)]
            cible=round(cible2*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeMelee :#on vérifie si on peut taper le mob
                degat.append[cible, self.meleeAttack(self.listEnnemie[cible].ac)]
            cible=round(cible3*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeMelee :#on vérifie si on peut taper le mob
                degat.append[cible, self.meleeAttack(self.listEnnemie[cible].ac)]
            cible=round(cible4*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeMelee :#on vérifie si on peut taper le mob
                degat.append[cible, self.meleeAttack(self.listEnnemie[cible].ac)]
            #c'est moche mais plus simple qu'un for dans ce cas
            return degat
        elif action<3/nombreAction:#attaque ranged
            degat=[]#chaque case contient 2 case, l'id de la cible, et les dégats qu'elle prend
            cible=round(cible1*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeRanged :#on vérifie si on peut taper le mob
                degat.append[cible, self.rangedAttack(self.listEnnemie[cible].ac)]
            cible=round(cible2*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeRanged :#on vérifie si on peut taper le mob
                degat.append[cible, self.rangedAttack(self.listEnnemie[cible].ac)]
            cible=round(cible3*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeRanged :#on vérifie si on peut taper le mob
                degat.append[cible, self.rangedAttack(self.listEnnemie[cible].ac)]
            cible=round(cible4*len(self.listEnnemie))
            if self.listeDistanceEnnemie[cible]<=self.rangeRanged :#on vérifie si on peut taper le mob
                degat.append[cible, self.rangedAttack(self.listEnnemie[cible].ac)]
            #c'est moche mais plus simple qu'un for dans ce cas
            return degat
        #chaque cas DOIT retourner quelque chose, même si c'est un simple string
        
    def IAChecking(self):
        #envoie tout entre 0 et 1
        #envoie entre 0 et 1 les distances des ennemies en X et Y (donc divisé par 1000)
        #ainsi que leurs vie normal divisé par 1000 et max par 1000 et leur AC divisé par 100
        #et idem sur le mob (sauf AC)
        #peut-etre plus tard la puissance de ces mobs ? ou leur vitesse ?
        #ça fait deja bcp d'input
        data=[self.life/1000, self.lifeMax/1000, self.position[0]/1000, self.position[1]/1000]
        for i in range(len(self.listEnnemie)):
            data.append(self.lisEnnemie[i].life/1000)
            data.append(self.lisEnnemie[i].lifeMax/1000)
            data.append(self.lisEnnemie[i].positionX/1000)
            data.append(self.lisEnnemie[i].positionY/1000)
            data.append(self.lisEnnemie[i].ac/100)
        return data
            
            
            
            
            