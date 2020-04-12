#JUAN JOSE GAMEZ RECHE
from ParticulaMasa import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from pymongo import MongoClient

class Simulacion_Mongo:
    num_particulas=0
    particulas=list()
    tiempoTot=0
    deltaT=0.02

    def __init__(self, tiempo_tot):
        self.tiempoTot=tiempo_tot
        
        #Lectura con Mongo
        cliente = MongoClient()
        db=cliente.ParticulasDB
        lista_particulas=db.Iniciales.find()
        particula_aux=ParticulaMasa()
        
        for elemento in lista_particulas:
            particula_aux.set_valores(self.conv_arr(elemento['pos']), self.conv_arr(elemento['vel']),
                                        self.conv_arr(elemento['acc']), elemento['masa'])
            particula_aux.muestra()
            self.particulas.append(particula_aux)
        
        self.num_particulas=len(self.particulas)
        print("El numero de particulas cargadas es: ", self.num_particulas)
        self.prepara_grafico()

    
    def avanza(self):
        for i in range(self.num_particulas):                                            #Inicializamos las aceleraciones a 0
            self.particulas[i].set_valores(self.particulas[i].pos, self.particulas[i].vel, np.array([0.0, 0.0, 0.0]), self.particulas[i].masa)
        
        for i in range(self.num_particulas):
            for j in range(self.num_particulas):
                if i != j:                                                              #Una partícula no causa aceleración a sí misma
                    self.particulas[i].aceleracion_gravitatoria(self.particulas[j])
        
        for i in range(self.num_particulas):
            self.particulas[i].actualiza_velocidad_y_posicion(self.deltaT)

                       
    def simula(self):
        for i in range(1,self.tiempoTot):
            self.avanza()
            self.refresca_particulas()
            self.guardar_valores(i)

        
        for i in range(self.num_particulas):
            self.particulas[i].muestra()


    def prepara_grafico(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')

        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)

        self.grafico=self.ax.scatter([],[],[],c='r',marker='o')


    def refresca_particulas(self):
         self.grafico.remove()
         col=['g']
         for _ in range(1, self.num_particulas):
             col.append('r')  
         x,y,z=self.vectoriza()
         self.grafico=self.ax.scatter(x,y,z,c=col,marker='o')
         plt.draw()
         plt.pause(0.1)


    def vectoriza(self):                            #Simplemente trasladamos las posiciones de las particulas a 3 vectores (x,y,z)
        x=list()
        y=list()
        z=list()

        for i in range(self.num_particulas):
            x.append(self.particulas[i].pos[0])

        for i in range(self.num_particulas):
            y.append(self.particulas[i].pos[1])
        
        for i in range(self.num_particulas):
            z.append(self.particulas[i].pos[2])

        return x,y,z


    def conv_arr(self, una_lista):
        arr_aux=np.array([0.0, 0.0, 0.0])
        arr_aux[0]=una_lista[0]
        arr_aux[1]=una_lista[1]
        arr_aux[2]=una_lista[2]
        return arr_aux
    
    #Guarda los datos de todas las partic(ulas para un instante determinado de tiempo
    def guardar_valores(self, t):
        cliente1=MongoClient()
        db=cliente1.ParticulasDB
        for i in range(self.num_particulas):
            db.Calculados.insert_one({"pos":self.particulas[i].pos, "acc":self.particulas[i].acc, 
                                        "vel":self.particulas[i].vel, "t":t})


        