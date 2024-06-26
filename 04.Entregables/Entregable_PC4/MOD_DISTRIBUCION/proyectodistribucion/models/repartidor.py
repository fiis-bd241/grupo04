from config.database import get_db_connection

class Repartidor:
    @staticmethod
    def authenticate(usuario, contraseña):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_repartidor FROM repartidor WHERE usuario = %s AND contraseña = %s", (usuario, contraseña))
        result = cursor.fetchone()
        connection.close()
        if result:
            return result[0]  # Devuelve el ID del repartidor si se encuentra
        return None


