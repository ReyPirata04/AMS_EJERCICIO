from .vehiculo import Vehiculo

#Clase automovil con su atributo y metodos
class Automovil(Vehiculo):
    ruedas = 4
    def __init__(self, año, color, marca, modelo, aceleracion, velocidad):
        super().__init__(año, modelo)
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def conducir(self):
        pass

    def acelerar(self):
        self.velocidad += self.aceleracion
        return self.velocidad

    def frenar(self):
        self.velocidad -= self.aceleracion
        return self.velocidad
