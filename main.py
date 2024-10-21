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
#Primera instancia coche, y mostrada por consola las ruedas y la aceleración
coche1 = Automovil("Negro","Chevrolet",5,100)

print("Ruedas",coche1.ruedas, "\n Aceleracion:", coche1.aceleracion)


#Aceleración modificada y mostrar por pantalla ambas aceleraciones
acleracion_mod = 10
coche1.aceleracion += acleracion_mod

print("Aceleracion agregada: ", acleracion_mod)
print("Aceleracion ya modificada: ",coche1.aceleracion)


#Creada la 2da instancia de la clase, frenao se muestran los resultados
coche2 = Automovil("blanco","ford", 7, 100)

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
        if self.esta_volando == True:
            print(f"El {self.marca} esta volando")
        else:
            print("El {self.marca} esta por volar")

    def aterriza(self):
        if self.esta_volando == False:
            print("El {self.marca} esta aterrizando")
        else:
            print("El {self.marca} esta por aterrizar")


Automovilvolador = AutomovilVolador("Blanco", "Tesla", 10, 200)

print(f"Marca del auto volador: {Automovilvolador.marca}")
print(f"Color del {Automovilvolador.marca} volador: {Automovilvolador.color}")
print(f"Cantidad de ruedas: {Automovilvolador.ruedas}")
print(f"Aceleración del {Automovilvolador.marca} volador: {Automovilvolador.aceleracion}")
print(f"Velocidad del {Automovilvolador.marca} volador: {Automovilvolador.velocidad}")

Automovilvolador.vuela()
Automovilvolador.aterriza()














