from abc import ABC, abstractmethod

#Clase Automóvil con su atributo y metodos
class Automovil(ABC):
    ruedas = 4
    def __init__(self,color,marca,aceleracion,velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    @abstractmethod
    def conducir(self):
        pass

    def acelerar(self):
        self.velocidad += self.aceleracion
        return self.velocidad

    def frenar(self):
        self.velocidad -= self.aceleracion
        return self.velocidad
