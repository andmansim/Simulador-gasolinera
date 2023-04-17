# Simulador-gasolinera

https://github.com/andmansim/Simulador-gasolinera.git
```
import threading
import random
import time



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
    t = random.randint(0, 15)
    time.sleep(t)
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
        
    def media(self):
        self.tiempo_total = self.t_caja + self.t_surtidor + self.t
        m = self.tiempo_total/3
        print(f'El coche {self.id} ha tardado {m}')
        
    def run(self):
        self.llegada()
        self.gasolina()
        self.caja()
        self.salida()
        self.media()
        

q = Cola()
semaforo = threading.Semaphore(1) #cerrado

for i in range(50):
    c = Cliente(i) #creamos hilos
    q.encolar(c) #Añadimos a al cola
    
for a in q.items:
    a.start()

```
