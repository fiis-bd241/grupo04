from config.database import get_db_connection

class Pedido:
    @staticmethod
    def obtener_pedidos_historial():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_pedido, id_venta, id_est_pedido FROM pedido WHERE id_est_pedido IN ('E', 'C')")
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos

    @staticmethod
    def obtener_pedidos_pendientes():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_pedido, id_venta, id_est_pedido FROM pedido WHERE id_est_pedido = 'P'")
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos
