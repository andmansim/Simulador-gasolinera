#indicar los estados: 
#coches hilos, 50 hilos
#tiempo 15 minutos, surtidores 1
#calcular el tiempo medio que tarda un coche
#pasar todos los cálculos a centensimas de segundo

#llegan coches cada 15 minutos, gasolinera 1 surtidor. 
#Coche en el surtidor tarda entre 5 y 10 minutos
#Después se va a pagar: se pone en la caja, solo hay 1, tarda 3 minutos
#Tras terminar se va

import threading
import random
import time

'''
Necesitamos: cola, cliente, gasolinera
'''
class Cola:
    def __ini__(self):
        self.datos = []
    
    def encolar(self, x):
        self.datos.append(x)
        
    def desencolar(self):
        try: return self.datos.pop(0)
        except: raise ValueError('La cola está vacia')
        
    def vacia(self):
        return self.datos == []

class Cliente(threading.Thread):
    
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.estado = None
        self.tiempo_total = 0
        self.t_surtidor = random.randint(5, 10)
        self.t_caja = 3
    
    def set_estado(self, nuevo):
        self.estado = nuevo
    
    def llegada(self):
        self.estado = 'Llego a la gasolinera'
    def gasolina(self):
        self.estado = 'Echando gasolina'
        time.sleep(self.t_surtidor/60)
    def caja(self):
        self.estado = 'Pagando'
        
    def salida(self):
        self.estado= 'Se va'
        
    
        
