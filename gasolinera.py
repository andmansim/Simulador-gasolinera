#indicar los estados: 
#coches hilos, 50 hilos
#tiempo 15 minutos, surtidores 1
#calcular el tiempo medio que tarda un coche
#pasar todos los cálculos a centensimas de segundo

#llegan coches cada 15 minutos, gasolinera 1 surtidor. 
#Coche en el surtidor tarda entre 5 y 10 minutos
#Después se va a pagar: se pone en la caja, solo hay 1, tarda 3 minutos
#Tras terminar se va
#Vista: empieza y sale
#Controlador: 

import threading
import random
import time

'''
Necesitamos: cola, cliente, gasolinera
'''



class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, x):
        self.items.append(x)
        
    def desencolar(self):
        try: return self.items.pop(0)
        except: raise ValueError('La cola está vacia')
        
    def vacia(self):
        return self.items == []

class Cliente(threading.Thread):
    global semaforo
    time.sleep(random.randint(0, 15))
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
        
        print(f'El coche {self.id} ha llegado a la gasolinera')
        semaforo.acquire()#Restamos y cerramos
        
    def gasolina(self):
        self.estado = 'Echando gasolina'
        print(f'El coche {self.id} está echando gasolina')
        time.sleep(self.t_surtidor)
        
        
    def caja(self):
        self.estado = 'Pagando'
        print(f'El coche {self.id} está pagando')
        time.sleep(self.t_caja)
        
    def salida(self):
        self.estado= 'Se va'
        print(f'El coche {self.id} se va')
        semaforo.release() #aumentamos
        
    def run(self):
        self.llegada()
        self.gasolina()
        self.caja()
        self.salida()
        

q = Cola()
semaforo = threading.Semaphore(1) #cerrado
for i in range(50):
    c = Cliente(i) #creamos hilos
    q.encolar(c) #Añadimos a al cola
    
for a in q.items:
    a.start()


