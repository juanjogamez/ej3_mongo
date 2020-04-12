#JUAN JOSE GAMEZ RECHE
from random import random, seed
import numpy as np

class Particula:
    __contador=0
    def __init__(self):
        self.pos=np.zeros(3)
        self.vel=np.zeros(3)
        self.acc=np.zeros(3)
        Particula.__contador += 1


    def set_valores(self, pPos, pVel, pAcc):
        self.pos=pPos
        self.vel=pVel
        self.acc=pAcc


    def init_random(self):
        self.set_valores(np.array([random(),random(),random()]),
                        np.array([random(),random(),random()]),
                        np.array([random(),random(),random()]) )


    def distancia(self, otra):
        delta=self.pos-otra.pos
        mod_distancia=((delta[0]**2)+(delta[1]**2)+(delta[2]**2))**(1/2)
        return mod_distancia

    
    def muestra(self):
        print("La posicion de la particula es",self.pos)
        print("La velocidad de la particula es",self.vel)
        print("La aceleracion de la particula es",self.acc)
        

    @classmethod
    def cuantosHay(cls):
        print("Se han definido :", cls.__contador)

