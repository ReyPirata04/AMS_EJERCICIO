# Creando conector y cursor
import sqlite3

conexion = sqlite3.connect("mi_bd.db")

cursor = conexion.cursor()

# Crear una tabla vehículo que contendrá los atributos
# correspondientes a la clase vehiculo
cursor.execute(
               '''
               CREATE TABLE IF NOT EXISTS vehiculo
               (
                id_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
                año INTEGER NOT NULL,
                modelo TEXT NOT NULL
               )
               '''
            )
# Crear un vehículo e insertarlo en la base de datos
vehiculos = [(2004, 'Volkswagen Polo Classic'),
             (2012, "Tesla S"),
             (2020, "Volkswagen ID.7")]

cursor.executemany("INSERT INTO vehiculo(año,modelo)VALUES(?,?)",vehiculos)

conexion.commit()

# Leer los vehículos de la base de datos y mostrarlo por pantalla
cursor.execute("SELECT * FROM vehiculo")

rows = cursor.fetchall()

print(rows)

cursor.close()
conexion.close()

