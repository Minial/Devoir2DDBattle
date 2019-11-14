#classe abstraite des différents mob,
#pour éviter d'avoir le meme code partout
import random


class Mob:
    def __init__(self, _x, _y, _la, _le, _size, _speed, _ac, _rangeMelee, _rangeRanged):
        self.size = _size
        self.position = [_x, _y]
        self.speed = _speed
        self.ac = _ac
        self.listAllies = _la
        self.listEnnemie = _le
        self.rangeMelee = _rangeMelee
        self.rangeRanged = _rangeRanged
        
        
    def meleeAttack(self, _ac, _taco, _diceNumber, _dicePower, _bonusDegat, _multiCrit=2, _critLuck=20): # Renvoie les dégats que fait le Mob
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
    
    def yolo(self):
        print("yolo")