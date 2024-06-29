from config.database import get_db_connection

class Persona:
    @staticmethod
    def authenticate(usuario, contraseña):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_cargo FROM persona WHERE usuario = %s AND contraseña = %s", (usuario, contraseña))
        result = cursor.fetchone()
        connection.close()
        if result:
            return Persona(id_cargo=result[0])
        return None
    
    def __init__(self, id_cargo):
        self.id_cargo = id_cargo
