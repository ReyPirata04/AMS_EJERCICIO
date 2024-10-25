from .figura import Figura

class Cuadrado(Figura):
    def __init__(self, lados):
        self.lados = lados

    #Área = (EL Cuadrado del cm de sus lados) 
    def area(self):
        area=self.lados**2
        return area
    
    #Perímetro = (Suma de sus cuatro lados iguales)
    def perimetro(self):
        perimetro = 4 * self.lados
        return perimetro