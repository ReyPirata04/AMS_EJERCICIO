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

class Coche(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad):
        super().__init__(color, marca, aceleracion, velocidad)

    def conducir(self):
        print(f"Conduciendo un {self.marca} de color {self.color}")

#Primera instancia coche, y mostrada por consola las ruedas y la aceleración
coche1 = Coche("Negro","Chevrolet",5,100)

print("Ruedas",coche1.ruedas, "\n Aceleracion:", coche1.aceleracion)


#Aceleración modificada y mostrar por pantalla ambas aceleraciones
acleracion_mod = 10
coche1.aceleracion += acleracion_mod

print("Aceleracion agregada: ", acleracion_mod)
print("Aceleracion ya modificada: ",coche1.aceleracion)


#Creada la 2da instancia de la clase, frenao se muestran los resultados
coche2 = Coche("blanco","ford", 7, 100)

frenada = coche2.frenar()

print("Esta es la velocidad del coche ford al frenar: ",frenada)


# Herencia en Python

#1-Crear clase AutomovilVolador que herede de Automovil con atributo de 6 ruedas

#2-Agregar al constructor esta_volando=True

#3-Agregar métodos vuela y aterriza(esta_volando)

#4-Crear un automovilvolador y muestre por consola comportamiento y características

class AutomovilVolador(Automovil):
    ruedas=6
    def __init__(self, color, marca, aceleracion, velocidad, esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad)
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


Automovilvolador = AutomovilVolador("Blanco", "Tesla", 10, 200)

print(f"Marca del auto volador: {Automovilvolador.marca}")
print(f"Color del {Automovilvolador.marca} volador: {Automovilvolador.color}")
print(f"Cantidad de ruedas: {Automovilvolador.ruedas}")
print(f"Aceleración del {Automovilvolador.marca} volador: {Automovilvolador.aceleracion}")
print(f"Velocidad del {Automovilvolador.marca} volador: {Automovilvolador.velocidad}")

Automovilvolador.vuela()
Automovilvolador.aterriza()

class Figura(ABC):

    @abstractmethod
    #Área = Base x Altura
    def area(self):
        pass

    @abstractmethod
    #Perímetro += (Cantidad De Lados)
    def perimetro(self):
        pass

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
    

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        area = 3.14 * self.radio**2
        return area
    
    def perimetro(self):
        perimetro = 2*self.radio*3.
        return perimetro
    

cuadrado1 = Cuadrado(5)

print(f"El perimetro del cuadrado es: {cuadrado1.perimetro()} ")
