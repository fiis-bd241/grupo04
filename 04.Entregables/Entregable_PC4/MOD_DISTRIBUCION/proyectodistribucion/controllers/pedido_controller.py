from config.database import get_db_connection

def obtener_historial_pedidos():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id_pedido, id_venta, id_est_pedido FROM pedido")
    result = cursor.fetchall()
    connection.close()
    pedidos = [{"id_pedido": row[0], "id_venta": row[1], "id_est_pedido": row[2]} for row in result]
    return pedidos

def obtener_pedidos_pendientes():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id_pedido, id_venta, id_est_pedido FROM pedido WHERE id_est_pedido = 'P'")
    result = cursor.fetchall()
    connection.close()
    pedidos = [{"id_pedido": row[0], "id_venta": row[1], "id_est_pedido": row[2]} for row in result]
    return pedidos
#aaa