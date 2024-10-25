from .figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        area = 3.14 * self.radio**2
        return area
    
    def perimetro(self):
        perimetro = 2*self.radio*3.
        return perimetro