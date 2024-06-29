import psycopg2

class ConexionDB():
    def __init__(self):
        self.conexion = psycopg2.connect(
            dbname = "MIGS Prov",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "8000"
    )
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()