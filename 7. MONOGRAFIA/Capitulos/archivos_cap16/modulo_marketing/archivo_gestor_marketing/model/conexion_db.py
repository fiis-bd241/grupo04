import psycopg2
from psycopg2 import sql

# Datos de conexión
DB_HOST = 'localhost'      # Reemplaza con el host de tu base de datos
DB_NAME = 'mignistore'    # Reemplaza con el nombre de tu base de datos
DB_USER = 'postgres'     # Reemplaza con tu nombre de usuario
DB_PASS = 'Aandy1502'  # Reemplaza con tu contraseña
DB_PORT = '5432'          # Reemplaza con el puerto de tu base de datos (el puerto predeterminado es 5432)

class conexionDB():
    def __init__(self):
        # Establecer la conexión
        self.conexion = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.cursor.close()
        self.conexion.close()


