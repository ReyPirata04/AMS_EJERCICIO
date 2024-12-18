from .autoMovil import Automovil

class AutomovilVolador(Automovil):
    ruedas=6
    def __init__(self, año, color, marca, modelo,aceleracion, velocidad, esta_volando=True):
        super().__init__(año,color, marca, modelo, aceleracion, velocidad)
        self.esta_volando = esta_volando

    def vuela(self):
        if self.esta_volando:
            print(f"El {self.marca} esta volando")
        else:
            print(f"El {self.marca} esta por volar")

    def aterriza(self):
        if self.esta_volando:
            self.esta_volando = False
            print(f"El {self.marca} esta aterrizando")
        else:
            print(f"El {self.marca} ya esta en tierra")

    def conducir(self):
        print(f"Conduciendo un {self.marca} volador de color {self.color}")

    def datos(self):
        return (f"Tipo de autovolador: {self._modelo}\nCantidad de ruedas: {self.ruedas}")
