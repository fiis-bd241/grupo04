import psycopg2

class ConexionDB():
    def __init__(self):
        self.conexion = psycopg2.connect(
            dbname = 'finanzas',
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "5432"
    )
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()