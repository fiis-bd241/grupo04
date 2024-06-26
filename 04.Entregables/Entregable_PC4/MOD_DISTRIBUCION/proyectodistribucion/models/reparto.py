from config.database import get_db_connection

class Reparto:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def get_repartidores(self):
        query = "SELECT * FROM Repartidor"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        self.cursor.close()
        self.conn.close()
