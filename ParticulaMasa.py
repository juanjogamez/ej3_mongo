#JUAN JOSE GAMEZ RECHE
from Particula import *

class ParticulaMasa(Particula):     #Herencia
        def __init__(self):
            super().__init__()      #Llamamos al init de la clase padre a traves de super()
            self.masa=0.0           #Añadimos el atributo masa, tomando por defecto el valor 0.0
        
        def set_valores(self, pPos, pVel, pAcc, masa):                      #Metodo redefinido
            super().set_valores(pPos, pVel, pAcc)
            self.masa=masa
        
        def init_random(self):                                              #Metodo redefinido
            self.set_valores(np.array([random(),random(),random()]),            
                        np.array([random(),random(),random()]),
                        np.array([random(),random(),random()]) ,random())
            
        
        def muestra(self):                                                  #Metodo redefinido
            super().muestra()                                               #Los atributos que no cambian, se muestran a traves del muestra de la clase super
            print("La masa de la particula es",self.masa)                   #Unicamente falta mostrar la masa
            print('\n')

        def aceleracion_gravitatoria(self, otra):                           
            G=6.67259e-11
            dx=float(self.pos[0]-otra.pos[0])
            dy=float(self.pos[1]-otra.pos[1])
            dz=float(self.pos[2]-otra.pos[2])
            dst_cubo=(self.distancia(otra))**3
            
            self.acc=self.acc + np.array([((-G)*otra.masa*dx)/dst_cubo,
                             ((-G)*otra.masa*dy)/dst_cubo,
                             ((-G)*otra.masa*dz)/dst_cubo])

        def actualiza_velocidad_y_posicion(self, deltat):
            vx=self.vel[0]+self.acc[0]*deltat
            vy=self.vel[1]+self.acc[1]*deltat
            vz=self.vel[2]+self.acc[2]*deltat

            px=self.pos[0]+self.vel[0]*deltat
            py=self.pos[1]+self.vel[1]*deltat
            pz=self.pos[2]+self.vel[2]*deltat
            
            self.set_valores(np.array([px, py, pz]), np.array([vx, vy, vz]), self. acc, self.masa)

