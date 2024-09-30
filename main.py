#Clase Automóvil con su atributo y metodos
class Automovil:
    ruedas = 4
    def __init__(self,color,marca,aceleracion,velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

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

