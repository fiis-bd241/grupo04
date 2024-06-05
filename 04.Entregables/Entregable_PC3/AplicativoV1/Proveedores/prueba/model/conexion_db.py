import psycopg2

class ConexionDB():
    def __init__(self, db_host, db_name, db_user, db_password, db_port):
        self.base_datos = 'database/peliculas.db'
        self.conexion = psycopg2.connect(
            host="localhost",
            database="PRUEBA123",
            user="postgres",
            password="1234",
            port = "5432"
        )
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()