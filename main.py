class Automovil:
    ruedas = 4
    def __init__(self,color,marca,aceleracion,velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelerar(velocidad,aceleracion):
        velocidad += aceleracion

    def frenar(velocidad, aceleracion):
        velocidad -= aceleracion

coche1 = Automovil("Negro","Chevrolet",5,100)

print("Ruedas",coche1.ruedas, "\n Aceleracion:", coche1.aceleracion)

acleracion_mod = 10
coche1.aceleracion += acleracion_mod

print("Aceleracion agregada: ", acleracion_mod)
print("Aceleracion ya modificada: ",coche1.aceleracion)

coche2 = Automovil("blanco","ford", 7, 100)

velocidad_coche2 = coche2.velocidad
aceleracion_coche2 = coche2.aceleracion

freno_coche2 = coche2.frenar(velocidad_coche2,aceleracion_coche2)

print("Resultado por frenar el coche 2 ", freno_coche2)


