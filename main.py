from Clases.automovilVolador import AutomovilVolador
from Clases.coche import Coche
from Clases.vehiculo import Vehiculo

#Primera instancia coche, y mostrada por consola las ruedas y la aceleración
coche1 = Coche(2000,"Negro","Chevrolet","CRUZE RS",5,100)

print("Ruedas",coche1.ruedas, "\nAceleracion:", coche1.aceleracion)


#Aceleración modificada y mostrar por pantalla ambas aceleraciones
acleracion_mod = 10
coche1.aceleracion += acleracion_mod

print("Aceleracion agregada: ", acleracion_mod)
print("Aceleracion ya modificada: ",coche1.aceleracion)


#Creada la 2da instancia de la clase, ya frenado, se muestran los resultados
coche2 = Coche(2010,"blanco","ford","MAVERICK", 7, 100)

frenada = coche2.frenar()

print("Esta es la velocidad del coche ford al frenar: ",frenada)

Automovilvolador = AutomovilVolador(2012,"Blanco", "Tesla", "Model S",10, 200)

print(f"Marca del auto volador: {Automovilvolador.marca}")
print(f"Color del {Automovilvolador.marca} volador: {Automovilvolador.color}")
print(f"Cantidad de ruedas: {Automovilvolador.ruedas}")
print(f"Aceleración del {Automovilvolador.marca} volador: {Automovilvolador.aceleracion}")
print(f"Velocidad del {Automovilvolador.marca} volador: {Automovilvolador.velocidad}")

Automovilvolador.vuela()
Automovilvolador.aterriza()

vehiculo1 = Vehiculo(2012,"Model S")

print("Año del vehiculo1:",vehiculo1.getAño())
print("Modelo del vehiculo1:",vehiculo1._modelo)

vehiculo1.setAño(2015)
vehiculo1._modelo = "Coupe"

print("Nuevo Año del vehiculo1:",vehiculo1.getAño())
print("Nuevo Modelo del vehiculo1:",vehiculo1._modelo)


def datosVehiculo(vehiculo):
    return vehiculo.datos()

print(datosVehiculo(Automovilvolador))
print(datosVehiculo(coche1))
print(datosVehiculo(coche2))

print("Tipo de clase: ", type(coche1))






