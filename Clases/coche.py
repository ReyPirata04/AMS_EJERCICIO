from .automovil import Automovil

class Coche(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad):
        super().__init__(color, marca, aceleracion, velocidad)

    def conducir(self):
        print(f"Conduciendo un {self.marca} de color {self.color}")
