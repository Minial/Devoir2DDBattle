#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    
    def __init__():
        listeMobs.append(Solar(500,250))
        print (listeMobs[0].life)
        
        for mob in listeMobs:
            if mob.life<=0 :
                del listeMobs[listeMobs.index(mob)]
        

            
    
        