"""
Created on Mon Nov  4 14:27:38 2019

@author: adrien
"""

from WorgRider import WorgRider
from Solar import Solar
from Warlord import Warlord
from Barbare import Barbare

class Terrain :
    tailleX = 1000
    tailleY = 1000
    listeMobs = []
    
    def __init__(self):
        self.listeMobs.append(Solar(500,250))
        print (self.listeMobs[0].life)
        
        
    def Tour(self):
        self.listeMobs[0].life=self.listeMobs[0].life-100
        print (self.listeMobs[0].life)
        for mob in self.listeMobs:
            if mob.life<=0 :
                print("il est mort !")
                del self.listeMobs[self.listeMobs.index(mob)]
            else:
                print("invaincu !")
    
        