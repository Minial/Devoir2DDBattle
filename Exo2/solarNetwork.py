#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:49:04 2019

@author: adrien
"""

from numpy import *
from random import *

class solarNetwork:
    #contient les poids des neurones
    
    def __init__(self):
        self.network=[10,10,10,10,7]
        self.layer1Input=[0]*self.network[0]#contient dans chaque case les différentes entrées de la couche 1 (la plus complexe)
        self.layer1Weight=[0]*self.network[0]#la couche 1 prend un nombre différents
        self.layer2Input=[0]*self.network[1]
        self.layer2Weight=[0]*self.network[1]
        self.layer3Input=[0]*self.network[2]
        self.layer3Weight=[0]*self.network[2]
        self.layer4Input=[0]*self.network[3]
        self.layer4Weight=[0]*self.network[3]
        self.layer5Input=[0]*self.network[4]
        self.layer5Weight=[0]*self.network[4]#faut pas oublier init des poids
        
 
    def neurone (self,inputN,weight):
        #on prend liste input et liste poids
        outputN=0
        for i in range (len(inputN)):
            outputN+=arctan(inputN[i]*weight[i])#on peut remplacer arctan par autre chose
        return outputN
    
    
    def reflection(self,inputNetwork):
        for i in range (len(inputNetwork)):#on prend les input qu'on met sur les input decouche 1
            self.layer1Input[i%self.network[0]].append(inputNetwork[i])
            #on ajoute a chaque neurone un input en plus
        for i in range (self.network[0]):
            #on fait calcul première couche
            temp=self.neurone(self.layer1Input[i], self.layer1Weight[i])
            self.layer2Input[i%self.network[1]].append(temp)
            #et on met dans input 2eme couche
        for i in range (self.network[1]):
            temp=self.neurone(self.layer2Input[i], self.layer2Weight[i])
            self.layer3Input[i%self.network[2]].append(temp)
            #et on met dans input 3eme couche
        for i in range (self.network[2]):
            temp=self.neurone(self.layer3Input[i], self.layer3Weight[i])
            self.layer4Input[i%self.network[3]].append(temp)
            #et on met dans input 4eme couche
        for i in range (self.network[3]):
            #attention couche 4 a 10 neurone et couche 5 en a 7
            #attention aux poids
            temp=self.neurone(self.layer4Input[i], self.layer4Weight[i])
            self.layer5Input[i%self.network[4]].append(temp)
            #et on met dans input 2eme couche
            outputNetwork=[]
        for i in range (self.network[4]):
            #dernière couche
            temp=self.neurone(self.layer5Input[i], self.layer5Weight[i])
            outputNetwork.append(temp)
            #et on met dans input 2eme couche
            
        def emptyWeight(self):
            #remplis les poids avec des aleatoires si layer1Weight vide
            if (self.layer1Weight==[0]*self.network[0]):
                maxWeight= 10.0
                minWeight= -10.0
                for i in range (self.network[0]):#première couche a 75 input
                    