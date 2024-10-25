from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    #Área = Base x Altura
    def area(self):
        pass

    @abstractmethod
    #Perímetro += (Cantidad De Lados)
    def perimetro(self):
        pass