#classe abstraite des différents mob,
#pour éviter d'avoir le meme code partout
import random
import numpy as np


class Mob:
    def __init__(self, _x, _y, _la, _le, _size, _speed, _ac, _rangeMelee, _rangeRanged, _numberMelee, _numberRanged, _color):
        self.color = _color
        self.size = _size#diametre du mob
        self.position = [_x, _y]
        self.destination = self.position
        self.speed = _speed#vitesse du mob, aussi la distance max qu'il peut faire par tour
        self.ac = _ac
        self.listAllies = _la
        self.listEnnemie = _le
        self.rangeMelee = _rangeMelee
        self.rangeRanged = _rangeRanged
        self.numberMelee = _numberMelee
        self.numberRanged = _numberRanged
        self.listeDistanceEnnemie = []#stock les distances des différents ennemies
        self.idNearestEnnemie = []
        self.tourMob=False#le mob est en train de faire son tour
        self.canMeleeAttack=False#le mob peut taper melee
        self.canRangedAttack=False#le mob peut taper ranged
        #stocke par ordre croisant de distance les id des différents ennemis
        self.name=self.__class__.__name__#peut servir ou pas
        
        
    def meleeAttack(self, _ac, _taco=10, _diceNumber=1, _dicePower=6, _bonusDegat=0, _multiCrit=2, _critLuck=20):
        # Renvoie les dégats que fait le Mob
        d20 = random.randint(1,20)#jet de toucher du mob
        if (d20 == 1):#echec critique on touche jamais
            return 0
        else :
            degats=0#les dégats renvoyé
            if (d20 >= _critLuck):#critique ! on touche a coup sur avec double de dgt
                degats = _bonusDegat*_multiCrit
                for i in range (_diceNumber*_multiCrit):
                    degats=degats+random.randint(1,_dicePower)
            elif (d20 + _taco > _ac):
                degats = _bonusDegat
                for i in range (_diceNumber):
                    degats=degats+random.randint(1,_dicePower)
            #dans les autres cas on touche pas
            return degats
    

    def rangedAttack(self, _ac, _taco=10, _diceNumber=1, _dicePower=6, _bonusDegat=0, _multiCrit=2, _critLuck=20):
        # Renvoie les dégats que fait le Mob
        d20 = random.randint(1,20)#jet de toucher du mob
        if (d20 == 1):#echec critique on touche jamais
            return 0
        else :
            degats=0#les dégats renvoyé
            if (d20 >= _critLuck):#critique ! on touche a coup sur avec double de dgt
                degats = _bonusDegat*_multiCrit
                for i in range (_diceNumber*_multiCrit):
                    degats=degats+random.randint(1,_dicePower)
            elif (d20 + _taco > _ac):#attaque normal
                degats = _bonusDegat
                for i in range (_diceNumber):
                    degats=degats+random.randint(1,_dicePower)
            #dans les autres cas on touche pas
            return degats
        
    def observationDistanceEnnemie(self, posi=[]):
        if posi==[]:#position par defaut est notre position
            posi=self.position
        #par defaut par rapport a notre position actuelle
        self.listeDistanceEnnemie=len(self.listEnnemie)*[0]
        #permet de garder en mémoire la distance de toutles ennemies
        self.idNearestEnnemie = []
        for i in range(len(self.listEnnemie)): # Calcul des distance avec les ennemies
            dx = posi[0] - self.listEnnemie[i].destination[0]
            dy = posi[1] - self.listEnnemie[i].destination[1]
            distance = np.sqrt(dx*dx + dy*dy)
            self.listeDistanceEnnemie[i]=[distance - self.size/2 - self.listEnnemie[i].size/2, distance]
            j=0
            while (j<len(self.idNearestEnnemie) and self.listeDistanceEnnemie[i][0]>
                   self.listeDistanceEnnemie[self.idNearestEnnemie[j]][0]):
                j+=1
            self.idNearestEnnemie.insert(j,i)#on ordonne la liste des mobs par distance
    
    def deplacement(self, idMobVise):
        self.observationDistanceEnnemie()
        
        distance=self.listeDistanceEnnemie[idMobVise]#indique la distance du mob visé
        #en 0 c'est celle entre les bords des mobs et en 1 entre leur centre

        Xtotal = self.listEnnemie[idMobVise].destination[0]- self.position[0]# selon thales c'est le X total
        Ytotal = self.listEnnemie[idMobVise].destination[1]- self.position[1]
        l=distance[1]
        dep=distance[0]#pensez a soustraire distance attack
        if (dep <= self.rangeMelee): # Distance inférieur à l'attque melee on ne se déplace pas
            self.destination = self.position
            self.canMeleeAttack=True
            self.canRangedAttack=True
            #print("le",self.name,"peut taper au cac sans deplacement")
            
        elif (dep <= self.speed + self.rangeMelee): # Déplacement en range melee (possibilité d'attaque)
            
            x = self.position[0] + (dep - self.rangeMelee)*Xtotal / l
            y = self.position[1] + (dep - self.rangeMelee)*Ytotal / l
            self.destination = [x,y]
            self.canMeleeAttack=True
            self.canRangedAttack=True
            #print("le",self.name,"peut taper cac avec deplacement")

        elif (dep <= self.speed + self.rangeRanged): # Déplacement en range distance (possibilité d'attaque)
            x = self.position[0] + (dep - self.rangeRanged)*Xtotal / l
            y = self.position[1] + (dep - self.rangeRanged)*Ytotal / l
            self.destination = [x,y]
            self.canMeleeAttack=False
            self.canRangedAttack=True
            #print("le",self.name,"peut taper distance avec deplacement")

        elif (dep <= 2*self.speed + self.rangeMelee): # Déplacement en range melee (impossible d'attaquer)
            x = self.position[0] + (dep - self.rangeMelee)*Xtotal / l
            y = self.position[1] + (dep - self.rangeMelee)*Ytotal / l
            self.destination = [x,y]
            #print("le",self.name,"peut pas taper cac avec deplacement (cac)")

        elif (dep <= 2*self.speed + self.rangeRanged): # Déplacement en range distance (impossible d'attaquer)
            x = self.position[0] + (dep - self.rangeRanged)*Xtotal / l
            y = self.position[1] + (dep - self.rangeRanged)*Ytotal / l
            self.destination = [x,y]
            #print("le",self.name,"peut pas taper distance avec deplacement (distance)")

        else : # Déplacement max
            x = self.position[0] + 2*self.speed*Xtotal/l
            y = self.position[1] + 2*self.speed*Ytotal/l
            self.destination = [x,y]
            #print("le",self.name,"peut pas taper avec deplacement")

        #print(self.destination)


    def deltaAction(self):
        if (self.position != self.destination):
            dx = self.position[0] - self.destination[0]
            dy = self.position[1] - self.destination[1]
            l = np.sqrt(dx*dx + dy*dy)
            px = dx*self.speed/12 / l
            py = dy*self.speed/12 / l
            if (self.speed/12 > l):
                #print("ok")
                self.position = self.destination
                #self.tourMob = False
            else :
                #print("dep")
                self.position = [self.position[0]-px, self.position[1]-py]
        else:
            for i in range(len(self.listEnnemie)):
                if (self.listEnnemie[i].life >0):
                    if (self.canMeleeAttack):
                        self.listEnnemie[i].life = self.listEnnemie[i].life - self.meleeAttack(self.listEnnemie[i].ac)
                    elif (self.canRangedAttack):
                        self.listEnnemie[i].life = self.listEnnemie[i].life - self.rangedAttack(self.listEnnemie[i].ac)
                    #print(self.listEnnemie[i].name, self.listEnnemie[i].life)
                    self.tourMob = False
                    return 0


    def hardIA(self):
        if (self.life<=0):
            #return "mort"
            return
        weakID = 0
        degat = []
        attaquePossible = 0
        for i in range (len(self.listEnnemie)):#on cherche le plus faible pour le taper
            if (self.listEnnemie[weakID].life>self.listEnnemie[i].life):
                weakID=i
        
        self.deplacement(weakID)
        self.observationDistanceEnnemie(self.destination)
        if (self.canMeleeAttack):
            #si on peut taper les mobs les plus proches cac, meme si pas le plus faible,
            #de toute façon il doit etre dedans
#self.listeDistanceEnnemie = []#stock les distances des différents ennemies
#self.idNearestEnnemie = []
            attaquePossible = self.numberMelee
            numberTemp=0
            nombreEnnemie = len(self.listEnnemie)
            print("Le", self.name, " peut taper cac")
            while (attaquePossible > 0 and numberTemp<len(self.listEnnemie) and
                   self.listeDistanceEnnemie[self.idNearestEnnemie[numberTemp]][0]<self.rangeMelee):
                #possibilité attaquer un mob
                if (self.listEnnemie[self.idNearestEnnemie[numberTemp]].life>0):
                    #on vas pas taper un mort
                    cible = self.listEnnemie[self.idNearestEnnemie[numberTemp]]
                    losedLife=self.meleeAttack(cible.ac)
                    degat.append([losedLife,cible])
                    print("le",self.name,"fait", losedLife, "dégat au cac à",cible.name)
                    self.listEnnemie[self.idNearestEnnemie[numberTemp]].life-=losedLife
                    attaquePossible-=1
                    if (cible.life-losedLife <= 0):#on check si mort
                        numberTemp+=1
                        nombreEnnemie-=1#il y a un ennemie en moins sur le terrain
                        print("Le", cible.name, " est mort !")
                else :#le mob est déjà mort
                    numberTemp+=1
            return degat
        elif (self.canRangedAttack):
            #si on peut taper les mobs les plus proches cac, meme si pas le plus faible,
            #de toute façon il doit etre dedans
#self.listeDistanceEnnemie = []#stock les distances des différents ennemies
#self.idNearestEnnemie = []
            attaquePossible = self.numberRanged
            numberTemp=0
            nombreEnnemie = len(self.listEnnemie)
            print("Le", self.name, " peut taper distance")
            while (attaquePossible > 0 and numberTemp<len(self.listEnnemie) and
                   self.listeDistanceEnnemie[self.idNearestEnnemie[numberTemp]][0]<self.rangeRanged):
                #possibilité attaquer un mob
                if (self.listEnnemie[self.idNearestEnnemie[numberTemp]].life>0):
                    #on vas pas taper un mort
                    cible = self.listEnnemie[self.idNearestEnnemie[numberTemp]]
                    losedLife=self.rangedAttack(cible.ac)
                    degat.append([losedLife,cible])
                    print("le",self.name,"fait", losedLife, "dégat à distance à",cible.name)
                    self.listEnnemie[self.idNearestEnnemie[numberTemp]].life-=losedLife
                    attaquePossible-=1
                    if (cible.life-losedLife <= 0):#on check si mort
                        numberTemp+=1
                        nombreEnnemie-=1#il y a un ennemie en moins sur le terrain
                        print("Le", cible.name, "est mort !")
                else :#le mob est déjà mort
                    numberTemp+=1
            return degat
        else:
            return "deplacement"

