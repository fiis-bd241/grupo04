# models/venta.py

from config.database import get_db_connection

class Venta:
    @staticmethod
    def obtener_compras_cliente(id_persona):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_venta, fecha_compra, total FROM venta WHERE id_persona = %s", (id_persona,))
        rows = cursor.fetchall()
        connection.close()
        return rows
