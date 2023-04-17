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

'''
Necesitamos: cola, cliente, gasolinera
'''
class Cola:
    def __ini__(self):
        self.datos = []
    
    def encolar(self, x):
        self.datos.append(x)
    def 
        