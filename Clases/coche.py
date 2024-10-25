from .autoMovil import Automovil

class Coche(Automovil):
    def __init__(self, año,color, marca, modelo,aceleracion, velocidad):
        super().__init__(año,color, marca, modelo,aceleracion, velocidad)

    def conducir(self):
        print(f"Conduciendo un {self.marca} de color {self.color}")
