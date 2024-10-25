from Clases.automovilVolador import AutomovilVolador
from Clases.coche import Coche
from Clases.cuadrado import Cuadrado

#Primera instancia coche, y mostrada por consola las ruedas y la aceleración
coche1 = Coche("Negro","Chevrolet",5,100)

print("Ruedas",coche1.ruedas, "\nAceleracion:", coche1.aceleracion)


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

Automovilvolador = AutomovilVolador("Blanco", "Tesla", 10, 200)

print(f"Marca del auto volador: {Automovilvolador.marca}")
print(f"Color del {Automovilvolador.marca} volador: {Automovilvolador.color}")
print(f"Cantidad de ruedas: {Automovilvolador.ruedas}")
print(f"Aceleración del {Automovilvolador.marca} volador: {Automovilvolador.aceleracion}")
print(f"Velocidad del {Automovilvolador.marca} volador: {Automovilvolador.velocidad}")

Automovilvolador.vuela()
Automovilvolador.aterriza()    

cuadrado1 = Cuadrado(5)

print(f"El perimetro del cuadrado es: {cuadrado1.perimetro()} ")
